#!/usr/bin/env python

from sys import argv
import os
import subprocess
from multiprocessing import Pool
from multiprocessing import cpu_count
import glob
import logging

logging.basicConfig(filename="logging.stdout", filemode='w', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def check_ref(reference):
    logging.info("Checking reference...")
    if not os.path.isfile(reference):
        logging.error(f"Reference {reference} not found. Exiting")
        exit
    elif not os.path.isfile(reference + ".ann"):
        my_env = os.environ.copy()
        args = ["bwa", "index", "-a", "bwtsw", reference]
        subprocess.run(args, shell=False, env=my_env)
        return reference
    return reference
    

def run_fq_qual(fname):
    
    my_env = os.environ.copy()
    args1 = ["fastq_quality_filter", "-i", fname, "q10", "-p90", "-Q33", "-v"]
    args2 = ["fastq_quality_filter", "-q20", "-p85", "-Q33"]
    args3 = ["fastq_quality_trimmer", "-t3", "-l40", "-Q33", "-v", "-o", fname + ".trim"]
    
    process_1 = subprocess.Popen(args1, stdout=subprocess.PIPE, shell=False, env=my_env)
    process_2 = subprocess.Popen(args2, stdin=process_1.stdout, stdout=subprocess.PIPE, shell=False, env=my_env)
    process_3 = subprocess.Popen(args3, stdin=process_2.stdout, stdout=subprocess.PIPE, shell=False, env=my_env)

    process_1.stdout.close()
    process_2.stdout.close()
    
    process_3.communicate()[0]

    return fname + ".trim"


def run_aln(fname):
    
    my_env = os.environ.copy()
    args = ["bwa", "aln", "-f", fname.rsplit(".", 1)[0] + ".sai", "-t", str(cpu_count()), ref, fname]
    
    subprocess.call(args, shell=False, env=my_env)
    
    logging.info(f"bwa aln was run with the following parameters:\n{args}")
    
    return os.path.abspath(fname.rsplit(".", 1)[0] + ".sai")


def run_samse(fname):

    my_env = os.environ.copy()
    args = ["bwa", "samse", "-f", fname.rsplit(".", 1)[0] + ".sam", ref, fname, fname.rsplit(".", 1)[0] + ".trim"]

    subprocess.call(args, shell=False, env=my_env)
    logging.info(f"bwa samse was run with the following parameters:\n{args}")
    return os.path.abspath(fname.rsplit(".", 1)[0] + ".sam")


def run_samtools_view(fname):
    
    my_env = os.environ.copy()
    args = f"samtools view -S -b {fname} > {fname.rsplit('.', 1)[0] + '.bam'}"
    
    p = subprocess.Popen(args, shell=True, env=my_env)
    os.waitpid(p.pid, 0)
    logging.info(f"samtools view was run with the following parameters:\n{args}")
    return os.path.abspath(fname.rsplit('.', 1)[0] + '.bam')


def run_picard(fname):

    my_env = os.environ.copy()
    args = ["picard", "SortSam", "INPUT=", fname, "OUTPUT=", fname.rsplit(".", 1)[0] + ".sorted.bam", "SORT_ORDER=coordinate", "VALIDATION_STRINGENCY=LENIENT"]

    subprocess.call(args, shell=False, env=my_env)
    logging.info(f"picard sortsam was run with the following parameters:\n{args}")
    return os.path.abspath(fname.rsplit(".", 1)[0] + ".sorted.bam")


def run_samtools_index(fname):

    my_env = os.environ.copy()
    args = ["samtools", "index", fname]

    subprocess.call(args, shell=False, env=my_env)
    logging.info(f"samtools index was run with the following parameters:\n{args}")
    with open("bamfiles.txt", "a+") as bamfiles:
        bamfiles.write(fname + "\n")
    return os.path.abspath(fname.rsplit("/", 1)[0] + "/bamfiles.txt")

if __name__ == "__main__":

    try:
        indir = argv[1]   
    except IndexError:
        indir = os.getcwd()
   
    ### ref has to be set or things will crash
    ref = check_ref(argv[2])

    file_list = glob.glob(os.path.join(indir, "*.fastq.pear.assembled.fastq"))
    num_proc = int(cpu_count() / 2)
    p = Pool(num_proc)
    dot_trim = p.map(run_fq_qual, file_list)
    aln_ret = []
    for i in dot_trim:
        aln_ret.append(run_aln(i))
    sam_files = p.map(run_samse, aln_ret)
    bam_files = p.map(run_samtools_view, sam_files)
    sorted_bam_files = p.map(run_picard, bam_files)
    bam_files_path = p.map(run_samtools_index, sorted_bam_files)
