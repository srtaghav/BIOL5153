#! /usr/bin/env python3
print('#! /bin/bash')

jobname = 'test'
queue = 'med16core'
fname = jobname
nodesn = 1
procn = 1
wall = 3 # this number is in hours

print('#SBATCH -J', fname)
print('#SBATCH --partition', queue)
print('#SBATCH -o', fname + '.txt')
print('#SBATCH -e', fname + '.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=srtaghav@uark.edu')  
print('#SBATCH --nodes=' + str(nodesn))
print('#SBATCH --ntasks-per-node=',procn)
print('#SBATCH --time=' + str(wall) + ':00:00')

print('export OMP_NUM_THREADS=32')
 
# load required modules
print('module load samtools')
print('module load jellyfish')
print('module load bowtie2')
print('module load salmon/0.8.2')
print('module load java')
 
# cd into the directory where you're submitting this script from
print('cd $SLURM_SUBMIT_DIR')

# copy files from storage to scratch
print('rsync -av RNA-R*.fastq.gz /scratch/$SLURM_JOB_ID')

# cd onto the scratch disk to run the job
print('cd /scratch/$SLURM_JOB_ID/')

# run the Trinity assembly
print('/share/apps/bioinformatics/trinity/trinityrnaseq-v2.11.0/Trinity --seqType fq --left RNA-R1.fastq.gz --right RNA-R2.fastq.gz --CPU 48 --max_memory 250G --trimmomatic --no_normalize_reads --full_cleanup --output trinity_Run2')
 
# copy output files back to storage
print('rsync -av trinity_Run2 $SLURM_SUBMIT_DIR')