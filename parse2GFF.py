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
parser.add_argument("fasta", help = 'name of the FASTA file')

# parse the arguments
args = parser.parse_args()

# read in FASTA file
genome = SeqIO.read(args.fasta, 'fasta')

print('Genome ID is, ', genome.id)
print('Genome Sequence is, ', genome.seq)
print('Genome length is, ', len(genome.seq))

#create a nested dictionary
CDSdict = defaultdict(dict)

#(base, fileext) = input.split('.')
#outfile = base + 'Indexed' + '.fasta'
#out = open(outfile, 'w')

# open and read in GFF file
with open(args.gff, 'r') as gff_in:
    # create a csv reader object
    reader = csv.reader(gff_in, delimiter = '\t')

    # loop over all the lines in our reader object (i.e., parsed file)
    for line in reader: 
        if not line:
            continue
        else:
            genus = line[0].split()[0]
            species = line[0].split()[1]
            features = line[2]
            startcoords = str(int(line[3]) - 1)
            endcoords = line[4]
            strand = line[6]
            separate = line[8].split(sep = ';')
            line[-1] = separate
            strconvert = str(separate)
        if features != 'CDS':
            continue
        else:
            cds = re.search('Gene\s(\S+)\s(\S+)?\s?(\d+)?', strconvert)
            genename = cds.group(1)
            exonnumber = cds.group(3)

        CDScoords = [strand, startcoords, endcoords]
        CDSdict[genename][exonnumber] = CDScoords
        def sort(item: dict):
            return {a: sort(b) if isinstance(b, dict) else b for a, b in sort(item.items())}

CDSsortdict =  sort(CDSdict)
CDSsortlist = list(CDSsortdict.items())

for i in CDSsortlist:
    gene = i[0]
    genedictionary = i[1]
    concatenate = ''

    for x, y in genedictionary.items():
        exonnumber = x
        strand = y[0]
        start = y[1]
        end = y[2]

        if strand == '+':
            sequence = genome.seq[int(start):int(end)]
            concatenate += sequence

        else:
            sequence = genome.seq[int(start):int(end)].reverse_complement()
            concatenate += sequence

print('>' + genus + ' ' + species + ' ' + gene)
print(concatenate)
print()