# DeepSeq
Ultra Deep Amplicon Sequencing Analysis of NPM1 gene

## Before you run this pipeline:

- Edit rawdata directory path (rawdata_dir) containing {sample}_L001_R*_001.fastq.gz files in config.yaml.

- Edit result directory path (result_dir) where results should be reported in config.yaml.

## To launch the pipeline:

module purge
module load singularity snakemake

## To dry run
sbatch launch_analysis.sh dryrun /path/to/result_dir


## To execute
sbatch launch_analysis.sh execute /path/to/result_dir
