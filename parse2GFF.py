#! /usr/bin/env python3

import csv
import argparse
from Bio import SeqIO
from collections import defaultdict
import re

#inputs: 1) GFF file, 2) corresponding genome sequence (FASTA format)
# create an argument parser object
parser = argparse.ArgumentParser(description = 'This script will parse a GFF file and extract each feature from the genome')

# add positional arguments
parser.add_argument("gff", help = 'name of the GFF file')
parser.add_argument("fasta", help = 'name of the FASTA/FSA file')

# parse the arguments
args = parser.parse_args()

# read in FASTA file
genome = SeqIO.read(args.fasta.rstrip(), 'fasta')

outfile = 'gene_seq_x.fasta'
out = open(outfile, 'w')

out.write('Genome ID is, ' + str(genome.id))
out.write('\n')
out.write('\n')
out.write('Genome Sequence is, ' + str(genome.seq))
out.write('\n')
out.write('\n')
out.write('Genome length is, ' + str(len(genome.seq)))
out.write('\n')
out.write('\n')

def rev_comp(genome_seq, strand):
    if strand == "-":
        return(genome_seq.reverse_complement())
    else:
        return(genome_seq)
        
CDSdict = defaultdict(dict)

# open and read in GFF file
with open(args.gff, 'r') as gff_in:
    # create a csv reader object
    reader = csv.reader(gff_in, delimiter = '\t')

    # loop over all the lines in our reader object (i.e., parsed file)
    for line in reader: 
        if not line:
            continue
        elif re.search('^#', line[0]):
            continue
        else:
            start = line[3]
            end = line[4]
            strand = line[6]
            species = line[0]
            feature = line[2]
            header = line[-1]
            attributes = line[8]
            exonnumber = re.search(r"exon\s(\d)", attributes)
            new_header = ">" + species.replace(" ", "_") + "_" + attributes.split()[1]

            if feature == "CDS":
                if(not exonnumber):
                    CDSdict[new_header] = rev_comp(genome.seq[int(start)-1:int(end)], strand)
                elif(not CDSdict[new_header]):
                    CDSdict[new_header] = [' ']*256
                    CDSdict[new_header][int(exonnumber[1])-1] = rev_comp(genome.seq[int(start)-1:int(end)], strand)
                else:
                    CDSdict[new_header][int(exonnumber[1])-1] = rev_comp(genome.seq[int(start)-1:int(end)], strand)

for a in CDSdict:
    CDSdict[a] = ''.join(str(exon) for exon in CDSdict[a])

for a, b in CDSdict.items():
    out.write(a)
    out.write(b)
    out.write('\n')
    out.write('\n')

out.close()