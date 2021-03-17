#! /usr/bin/env python3

# This script generates a pbs file for the AHPCC Razor cluster

# define some variables
jobname = 'test'
queue = 'med16core'
fname = jobname
nodesn = 1
procn = 1
wall = 3 # this number is in hours

# This section prints the header/required info for the PBS script

print('#PBS -N', jobname) # job name
print('#PBS -q', queue) # which queue to use
print('#PBS -j oe') # join the STDOUT and STDERR into a single file
print('#PBS -o', str(fname) + '.$PBS_JOBID') # set the name of the job output file
print('#PBS -l nodes=' + str(nodesn) + ':ppn=' + str(procn)) # how many resources to ask for (nodes = num nodes; ppn = num processors)
print('#PBS -l walltime=' + str(wall) + ':00:00') # set the walltime (default to 1 hr)
print()

# cd into working directory
print('cd $PBS_O_WORKDIR')
print()

# load the necessary modules
print('# load modules')
print('module purge')
print('module load gcc/7.2.1 python/3.6.0-anaconda java/sunjdk_1.8.0 blast mafft/7.304b')
print()

# commands for this job
print('# insert commands here')
