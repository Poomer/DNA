import dna
import random



seq_l = []
seq_dict = {}

#class Dna_Sequence_Detector():
#"""This class detect the longest sequence and return the position of that longest one detected."""

#	def __init__(self):

dna1 = dna.DNA(10)
dna1.DnaGen()
dna1.PrintDna()
counter = 0


#for acid in dna1.sequence:
#print("ENTERING FOR LOOP ")
#start_acid = dna1.sequence
start_acid = 'AAAAAAAAACCAAAAAGGGGGGGGGGGAAAA'
print("start_acid : " + start_acid)

seq = ''

for pos in range(0,len(start_acid)-1):

	#if(pos == len(start_acid)-1):					### Last acid of the sequence
	#	break
	#else:
		if (start_acid[pos+1] == start_acid[pos]) and (len(seq)==0):    ### Plausible firstsequence detected
			seq = start_acid[pos:pos+1]
			print("first seq work")
			first_pos = pos
			print(first_pos)
			seq_l.append(pos)
		elif(start_acid[pos+1] == start_acid[pos]):					### if continues, just add it
			seq += start_acid[pos+1]
			print("continue seq")
			print(seq)
		else:														### Reset seq and push it to seq_list
			seq_l.append(seq)
			print("seq end")
			seq = ''

print(seq_l)






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
	

	





