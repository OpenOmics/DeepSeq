#!/usr/bin/env python

import os
from sys import argv
from multiprocessing import Pool
from multiprocessing import cpu_count
import pandas as pd
import subprocess
import datetime

# Main worker function which converts the bamfiles to sam and looks (in npm_sequences.py dicts) for each of the mutations and wiltypes sequences in those sam files
# and just adds up how many of each it finds
def main_worker(bamfile):
    import npm_seq
    my_env = os.environ.copy()
    mut_dict = npm_seq.mut_dict
    wildtypes = npm_seq.wildtypes # This line is new
    mut_list = npm_seq.mut_list
    print(f"running command: {['samtools', 'view', bamfile, '-o', bamfile.rsplit('.', 1)[0] + '_tmp.sam']}")
    subprocess.call(["samtools", "view", "-o", bamfile.rsplit(".", 1)[0] + "_tmp.sam", bamfile], shell=False, env=my_env)
    tmpsam = os.path.abspath(bamfile.rsplit(".", 1)[0] + "_tmp.sam")
    filename = bamfile.rsplit("/", 1)[1]
    filename = filename.split(".", 1)[0]
    filename = filename.split("_", 1)[1]
    count_mut = {}
    count_wt = {}
    totreads = 0

    for name in mut_list:
        count_mut[name] = 0
        count_wt[name] = 0

    with open(tmpsam, "r") as open_tmpsam:
        sam_list = open_tmpsam.read().splitlines()
        for sam_line in sam_list:
            totreads += 1
            cur_seq = sam_line.split("\t")[9]
            for mutname in mut_list:
                mutstr = mut_dict[mutname][0]
                wtstr = wildtypes[int(mut_dict[mutname][1])]
                if mutstr.upper() in cur_seq:
                    count_mut[mutname] += 1
                elif wtstr.upper() in cur_seq:
                    count_wt[mutname] += 1

    subprocess.call(["rm", tmpsam], shell=False, env=my_env)
    return filename, totreads, count_mut, count_wt, mut_list


# This function will create separate csv files for all samples conaining only the mutation types which have been detected in the sample
# and return a list of paths to all those files to be used in the merge_csv function
def create_csv(samples):    
    import csv
    dataframes = []
    all_csv_files = []
    attachment_all_csv_files = []
    all_tsv_files = []
    for sample in samples:
        fname = sample[0]
        totreads = sample[1]
        muts = sample[2]
        wts = sample[3]
        mutnames = sample[4]
        combined = {}
        for key in mutnames: # check each mutation name
            if int(muts[key]) > 0: # if the mutation isnt found, skip it
                # This puts values into the combined dict. The values are lists with [total reads, mutation count, wt count, 100 * (wt count + mutation count)]
                combined[key] = [totreads, muts[key], wts[key], '{0:.10f}'.format(100 * (float(muts[key]) / (float(wts[key]) + float(muts[key]))))]

        pd_mut = pd.DataFrame.from_dict(combined, orient='index', columns=[f"totreads: {totreads}", "mutated", "wildtype", "%mut"])
        pd_mut.index.name = fname
        with open(str(fname) + ".csv", "w") as csv_out:
            pd_mut.to_csv(csv_out, sep=',', decimal='.', header=fname, quotechar='"', quoting=csv.QUOTE_ALL)
            all_csv_files.append(os.path.abspath(str(fname) + ".csv"))
        with open("attachment_" + str(fname) + ".csv", "w") as csv_attachment:
            pd_mut.to_csv(csv_attachment, sep=';', decimal=',', header=fname, quoting=csv.QUOTE_NONE)
            attachment_all_csv_files.append(os.path.abspath("attachment_" + str(fname) + ".csv"))
        with open(str(fname) + ".tsv", "w") as tsv_out:
            pd_mut.to_csv(tsv_out, sep='\t', decimal='.', header=fname, quoting=csv.QUOTE_NONE)
            all_tsv_files.append(os.path.abspath(str(fname) + ".tsv"))
    return all_csv_files, attachment_all_csv_files, all_tsv_files


# This function will create a single csv file out of all the others 
def merge_csv(filelist, outfilename="NPM1_" + datetime.datetime.now().strftime("%y%m%d") + "_all_samples.csv"):
    with open(outfilename, "a+") as mergefile:
        for csvfile in filelist:
            cur_fn = csvfile.rsplit("/", 1)[1]
            cur_fn_noext = cur_fn.rsplit(".", 1)[0]
            with open(csvfile, "r") as a:
                for line in a:
                    mergefile.write(line)
                if filelist[-1] not in csvfile:
                    mergefile.write("\n")
    return outfilename


# Currently unused. Can be used to fix the exponent for export into CLC. Cannot be used since yhe new csv looks completely different
def exponent_fix(input_file, output):
    
    import csv

    with open(input_file, 'r') as inp:
        reader = list(csv.reader(inp, delimiter=";"))
        with open(output, 'w') as out:
            writer = csv.writer(out, quotechar='"', quoting=csv.QUOTE_ALL, delimiter=",")
            for row in reader:
                if len(row) < 1 or "totreads:" in row[1]:
                    writer.writerow(row)
                else:
                    newrow = row[0:1] + [it.upper() for it in row[1:]]
                    writer.writerow(newrow)
    return output

def send_mail(subj, body, bifogad_fil, recipients=[], sender='NPM1@gu.se'):
    from marrow.mailer import Mailer, Message
    """Send mail to specified recipients."""
    recipients = [*recipients]
    mailer = Mailer(dict(
        transport=dict(use='smtp',
                       host='change.me.se')))

    mailer.start()
    message = Message(
        subject=f'{subj}',
        plain=f'{body}',
        author=sender,
        to=recipients,)
    message.attach(str(bifogad_fil))
    mailer.send(message)
    mailer.stop()


if __name__ == "__main__":
    
    filelist = argv[1]
    run_name = str(argv[2]).split("/")[-1]
    
    try:    
        email = list(argv[3].split(","))
    except:
        email = []
    with open(filelist, "r") as sorted:
        bam_list = sorted.read().splitlines()
    p = Pool(cpu_count())
    work_done = p.map(main_worker, bam_list)
    print(work_done)
    print("list length: " + str(len(work_done)) + "\n")
    print("tuple length: " + str(len(work_done[0])) + "\n")
    print("dict length: " + str(len(work_done[0][2])) + "\n")
    all_csv_files = create_csv(work_done)
    print(all_csv_files)
    merge_csv(all_csv_files[0], "NPM1_all_samples.csv")
    merge_csv(all_csv_files[2], "NPM1_UDS_final_result.tsv")
    to_mail = merge_csv(all_csv_files[1], f"NPM1_{run_name}_" + datetime.datetime.now().strftime("%y%m%d") + ".csv")
    
    ### Feel free to customise mailsubject and mailbody to your liking
    mailsubject=f"NPM1 analysis report on run: {run_name}"
    mailbody = f"""
Your NPM1 analysis is complete!

The resulting csv is attached to this email

Have a pleasant day!
/Clinical Genomics Gothenburg\n\n
    """
    if len(email) > 0:
        send_mail(mailsubject, mailbody, to_mail, email)
        exponent_fix(to_mail, f"CLC_{to_mail}")
