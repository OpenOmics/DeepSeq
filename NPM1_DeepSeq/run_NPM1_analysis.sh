#!/bin/bash -l

HELP="\nUsage: run_NPM1_analysis.sh [OPTIONS] 
Options:\n
    -f    [absolute path to directory containing fastq.gz files]

    -o    [abolute path to output directory]

    -r    [absolute path to human reference fasta]
    -t    [temporary directory]
    -e    [email adress to be used]
          (this option requires configuration)\n\n"


scriptdir="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

DATE=$(date +"%Y_%m_%d_%H_%M_%S")

while getopts :f:o:r:e:h opt; do
    case $opt in
        f)
            echo "-f (fastq directory) was input as $OPTARG"
            FASTQDIR=$OPTARG
        ;;
        o)
            echo "-o (output directory) was input as $OPTARG"
            OUTDIR=$OPTARG
        ;;
        r)
            echo "-r (reference fasta) was input as $OPTARG"
            REF=$OPTARG
        ;;
        t)
            echo "-t (temporary dir) was input as $OPTARG"
            TEMP=$OPTARG
        ;;
        e)
            echo "-e (email adress) was input as $OPTARG"
            EMAILS=$OPTARG
        ;;
        h)
            printf "$HELP"
            exit 0
        ;;
        \?)
            echo "Invalid option: -$OPTARG" >&1
            echo "Type $0 -h for usage"
            exit 1
        ;;
    esac
done

echo "Starting NPM1 anaysis on $HOSTNAME  ..."

# Creates a Conda environment named NPM_DeepSeq which contains the required programs
echo "Establishing conda environment at `date` ..."
conda env create -f $scriptdir/environment.yaml 2> /dev/null
echo "... Done at `date`"

TMPDIR=$TEMP/tmp_NPM1_$DATE

MYNAME=$(basename $FASTQDIR)

script1=$scriptdir/pear.py
script2=$scriptdir/pipeline_amplicon_pear.py
script3=$scriptdir/npm_var.py

# Copies the fastq files to tmp directory to prepare to start working
mkdir -p $TMPDIR
echo "Copying $FASTQDIR/*.fastq.gz to $TMPDIR"
for file in $(ls $FASTQDIR/*.fastq.gz) ; do
    cp $file $TMPDIR
done

ls $TMPDIR/*.fastq.gz > $TMPDIR/files.txt
cd $TMPDIR

# Gunzips and runs PEAR on the samples
echo "Running: $PYTHON $script1 $TMPDIR/files.txt"
conda run -n NPM1_DeepSeq $script1 $TMPDIR/files.txt

# Does QC, mapping etc
echo "Running: $PYTHON $script2 $TMPDIR"
conda run -n NPM1_DeepSeq $script2 $TMPDIR $REF

# bamfiles.txt is just a file that contains all the sorted bamfile from the previous step.
# $FASTQDIR is used for providing context to the mail attachment in the for of run name
# Email server etc. has to be edited in npm_var.py in order to be used. By default,
# no emails will be sent if no adresses are given
echo "Running: $PYTHON $script3 $TMPDIR/bamfiles.txt $FASTQDIR $EMAILS"
conda run -n NPM1_DeepSeq $script3 $TMPDIR/bamfiles.txt $FASTQDIR $EMAILS

STAMP=$(date +"%y%m%d_%H%M")

# Uncomment the following block to get all of the csv files into the results directory
#echo "Copy loop"
#filestocopy=$(ls $TMPDIR | grep ".csv")
#for csv in $filestocopy ; do
#    echo "Copying $csv to $OUTIDIR"
#    cp $csv $OUTDIR
#done

echo "Copying single csv file to outdir"
cp $TMPDIR/NPM1_UDS_final_result.tsv $OUTDIR/NPM1_UDS_final_result_${MYNAME}.tsv

#Remove everything in tmpdir, leaving only results.
rm -rf $TMPDIR

echo "Done at `date` ! Your output is located here: $OUTDIR/NPM1_UDS_final_result_${MYNAME}.tsv"
