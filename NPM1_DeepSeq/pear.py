#!/usr/bin/env python

from sys import argv
from subprocess import call
from multiprocessing import cpu_count
import gzip
import shutil
from os import path
from os import environ

#The infile needs to be a text file which contains the output of "ls" where the fastq files are located
def unzipper(infile):
    filelist = []
    with open(infile, "r+") as fastqs:
        fqlist = iter(fastqs.readlines())
        fqzip = zip(fqlist, fqlist)
        for filepairs in fqzip:
            file1 = filepairs[0].rstrip()
            file2 = filepairs[1].rstrip()
            with gzip.open(file1, "rb") as f_in, open(f"uncompressed_{path.basename(file1)}"[:-3], "wb+") as f_out:
                shutil.copyfileobj(f_in, f_out)
                filelist.append(f"uncompressed_{path.basename(file1)}"[:-3])
            with gzip.open(file2, "rb") as r_in, open(f"uncompressed_{path.basename(file2)}"[:-3], "wb+") as r_out:
                shutil.copyfileobj(r_in, r_out)
                filelist.append(f"uncompressed_{path.basename(file2)}"[:-3])
    return filelist


def run_pear(fq):
    my_env = environ.copy()
    for fileitem in fq[::2]:
        file1 = str(fq.pop(0))
        file2 = str(fq.pop(0))
        call(["pear", "-f", file1, "-r", file2, "-j", str(cpu_count()), "-o", file1 + ".pear"], shell=False, env=my_env)

if __name__ == "__main__":
    infile = str(argv[1])
    run_pear(unzipper(infile))
