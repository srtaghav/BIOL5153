#! /usr/bin/env python3

# set the name of input DNA sequence file
filename = "nad4L.fasta"

# open the input file, assign to file handle called 'infile'
infile = open(filename, 'r')

#print(infile)

# read the file
dna_sequence = infile.read() # can add .rstrip after read() here
dna_sequence = dna_sequence.rstrip() # remove carriage returns

# close the file
infile.close()

seqlen = len(dna_sequence)

print("Length of DNA sequence:", seqlen)

#print(dna_sequence.count('A'))
numA = dna_sequence.count('A')

#print(dna_sequence.count('G'))
numG = dna_sequence.count('G')

#print(dna_sequence.count('T'))
numT = dna_sequence.count('T')

#print(dna_sequence.count('C'))
numC = dna_sequence.count('C')

sumAGTC = numA + numG + numT + numC

freqA = numA / sumAGTC
freqG = numG / sumAGTC
freqT = numT / sumAGTC
freqC = numC / sumAGTC

SumOfFreq = freqA + freqG + freqT + freqC

ATCont = freqA + freqT
GCCont = freqG + freqC

print("The number of A's in", filename + ":", numA)
print("The number of G's in", filename + ":", numG)
print("The number of T's in", filename + ":", numT)
print("The number of C's in", filename + ":", numC)

print("The frequency of A's in", filename + ":", freqA)
print("The frequency of G's in", filename + ":", freqG)
print("The frequency of T's in", filename + ":", freqT)
print("The frequency of C's in", filename + ":", freqC)

outfile = open('nad4L_output.txt', 'w')

outfile.write('DNA sequence: ' + dna_sequence + '\n')
outfile.write('\n')
outfile.write('Sequence length: ' + str(seqlen) + ' nt' + '\n')
outfile.write('\n')
outfile.write("Number of A's: " + str(numA) + '\n')
outfile.write("Number of G's: " + str(numG) + '\n')
outfile.write("Number of T's: " + str(numT) + '\n')
outfile.write("Number of C's: " + str(numC) + '\n')
outfile.write('\n')
outfile.write("Frequency of A's: " + str(freqA) + '\n')
outfile.write("Frequency of G's: " + str(freqG) + '\n')
outfile.write("Frequency of T's: " + str(freqT) + '\n')
outfile.write("Frequency of C's: " + str(freqC) + '\n')
outfile.write('\n')
outfile.write("Sum of Frequencies: " + str(SumOfFreq))
outfile.write('\n')
outfile.write("G + C content: " + str(GCCont) + '\n')
outfile.write("A + T content: " + str(ATCont) + '\n')

outfile.close()
