# DeepSeq
Ultra Deep Amplicon Sequencing Analysis of NPM1 gene

## How to run this pipeline:

[+] Edit rawdata directory path (rawdata_dir) containing {sample}_L001_R*_001.fastq.gz files in config.yaml.
[+] Edit result directory path (result_dir) where results should be reported in config.yaml.
[+] Launch the pipeline:

module purge
module load singularity snakemake

## To dry run
sbatch ~/project/methyl-seek-main/pipeline_submit.sh dryrun /path/to/result_dir


## To execute
sbatch ~/project/methyl-seek-main/pipeline_submit.sh execute /path/to/result_dir
