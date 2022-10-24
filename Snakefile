#####################################################################################################
# NPM1_ DeepSeq analyses
#
# Last Modified: October, 2022
#
#####################################################################################################

from os.path import join
from snakemake.io import expand, glob_wildcards
from snakemake.utils import R
from os import listdir
import pandas as pd

configfile: "config.yaml"

# Global workflow variables
sample_file= config["samples"]
rawdata_dir= config["rawdata_dir"]
working_dir= config["result_dir"]

# References
hg38_fa= config["hg38_fa"]


SAMPLES, = glob_wildcards(join(rawdata_dir, '{samples}_L001_R2_001.fastq.gz'))

rule all:
    input:
      expand(join(working_dir, "{samples}/NPM1_out/NPM1_UDS_final_result_{samples}.tsv"), samples=SAMPLES),


## Copy each FASTQ pair to new sample directory and run DeepSeq
rule run_DeepSeq:
    input:
      in = join(rawdata_dir, "{samples}_L001_{rn}_001.fastq.gz")
    output:
      smlink = join(working_dir, "{samples}/{samples}_L001_{rn}_001.fastq.gz"),
      out = join(working_dir, "{samples}/NPM1_out/NPM1_UDS_final_result_{samples}.tsv"),
    params:
      rname="run_DeepSeq",
      dir=directory(join(working_dir, {samples})),
      tag="{samples}",
      batch='--cpus-per-task=8 --mem=100g --time=2-00:00:00 --partition=norm --gres=lscratch:200',
    threads:
      2
    shell:
      """
      mkdir -p {params.dir}
      mkdir -p {params.dir}/NPM1_out
      ln -s {input.in} {output.smlink}

      ./Scripts/run_NPM1_analysis.sh -f {params.dir} -o {params.dir}/NPM1_out -t /lscratch/$SLURM_JOBID/ -r hg38_fa
      """
