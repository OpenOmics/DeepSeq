# DeepSeq
Ultra Deep Amplicon Sequencing Analysis of NPM1 gene

## Before you run this pipeline:
- Your rawdata file names should have following format: {sample}_L001_R*_001.fastq.gz
- Edit rawdata directory path (rawdata_dir) containing {sample}_L001_R*_001.fastq.gz files in config.yaml.
- Edit result directory path (result_dir) where results should be reported in config.yaml.

## To setup the pipeline:
```
cd ~/project_directory
git clone https://github.com/OpenOmics/DeepSeq.git
cd ~/project_directory/DeepSeq
```

### edit config.yaml
```
rawdata_dir: ~/project_directory/DeepSeq/rawdata #### Update this path to your rawdata folder
result_dir: ~/project_directory/DeepSeq/output #### Update this path to your project folder
hg38_fa: /data/OpenOmics/references/DeepSeq/hg38/Homo_sapiens_assembly38.fasta
```

## To dry run
```
sinteractive --mem=4g --cpus-per-task=4
module purge
module load singularity snakemake
cd ~/project_directory/DeepSeq
bash launch_analysis.sh dryrun ./
```

## To execute
```
cd ~/project_directory/DeepSeq
sbatch launch_analysis.sh execute ./
```
