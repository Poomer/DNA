import dna
import random

### DNA Sequene Dictionary ###
seq_dict = {}


### Test DNA ###
dna_length = int(input("Define the length of DNA"))
dna1 = dna.DNA(dna_length)
dna1.DnaGen()
dna1.PrintDna()


def sequence_detect(dna_seq):

	seq = ''
	first_pos = 0
	
	for pos in range(0,len(dna_seq)-1):

		if (dna_seq[pos+1] == dna_seq[pos]) and (len(seq)==0):    ### Plausible first sequence detected
			seq = dna_seq[pos]
			print("at position %d : first seq work" % pos)
			first_pos = pos
			print(first_pos)
			if(pos==len(dna_seq)-2):                                 ### If it is the penultimate one, always add another acid.
				seq +=seq
			seq_dict[first_pos] = seq


			## In case this is the last sequence

		elif(dna_seq[pos+1] == dna_seq[pos]):						### if continues, just add it
			seq += dna_seq[pos+1]
			print("at position %d : continue seq"% pos)
			print(seq)
			if(pos==len(dna_seq)-2):                                 ### If it is the penultimate one, always add another acid.
				seq +=dna_seq[pos]
			seq_dict[first_pos] = seq

		
			### Reset seq and push it to seq_list
		else:														
			if len(seq)!=0:
				seq_dict[first_pos] = seq+seq[0]
			print("at position %d : seq end"%pos)
			seq = ''

	print(seq_dict)

def longest_sequence():
	print ("Function longest_sequence() called")
	longest_pos = 0
	longest_seq = ''

	for key,value in seq_dict.items():
		print (key, value)
		if len(value)>len(longest_seq):     ## update the longest sequence found, along with its position
	 		longest_pos = key
	 		longest_seq = value
	print ("The longest sequence found at position %d with a sequence of %s" %(longest_pos,longest_seq))


sequence_detect(dna1.sequence)
longest_sequence()

	





