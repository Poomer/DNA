import dna
import random



seq_l = []
seq_dict = {}

#class Dna_Sequence_Detector():
#"""This class detect the longest sequence and return the position of that longest one detected."""

#	def __init__(self):

dna1 = dna.DNA(20)
dna1.DnaGen()
dna1.PrintDna()
counter = 0


#for acid in dna1.sequence:
#print("ENTERING FOR LOOP ")
start_acid = dna1.sequence
#start_acid = 'AAGCCCCCCGCACAATTTTTT'
print("start_acid : " + start_acid)

seq = ''
first_pos = 0


for pos in range(0,len(start_acid)-1):

		if (start_acid[pos+1] == start_acid[pos]) and (len(seq)==0):    ### Plausible first sequence detected
			seq = start_acid[pos]
			print("at position %d : first seq work" % pos)
			first_pos = pos
			print(first_pos)
			if(pos==len(start_acid)-2):                                 ### If it is the penultimate one, always add another acid.
				seq +=seq
			seq_dict[first_pos] = seq


			## In case this is the last sequence

		elif(start_acid[pos+1] == start_acid[pos]):						### if continues, just add it
			seq += start_acid[pos+1]
			print("at position %d : continue seq"% pos)
			print(seq)
			if(pos==len(start_acid)-2):                                 ### If it is the penultimate one, always add another acid.
				seq +=start_acid[pos]
			seq_dict[first_pos] = seq

		
			### Reset seq and push it to seq_list
		else:														
			if len(seq)!=0:
				seq_dict[first_pos] = seq+seq[0]
			print("at position %d : seq end"%pos)
			seq = ''

print(seq_dict)






"""
for acid in range(0,len(start_acid.sequence))
	if(counter != len(dna1.sequence)):
		if(dna1.sequence[counter+1] == dna1.sequence[counter]):
			start_acid += dna1.sequence[counter+1]
			print(start_acid)
		else:
			start_acid = dna1.sequence[counter]
			print(start_acid)
		counter += 1
		print(counter)
	else:
		break
"""	
	

	





