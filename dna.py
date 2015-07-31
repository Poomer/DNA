import random

class DNA():
	"""This module creates a dna sequence """

	acid = ['A','C','G','T']
	sequence = ''

	
	def __init__(self, DNA_length):
		self.DNA_length = DNA_length

	def DnaGen(self):
		#string_length = input("Define the lenght of your sample DNA")
		for i in range(self.DNA_length):
			num = random.randrange(0,3)
			if(num%4==1):
				self.sequence += self.acid[0]
			elif(num%4==2):
				self.sequence += self.acid[1]
			elif(num%4==3):
				self.sequence += self.acid[2]
			else:
				self.sequence += self.acid[3]

	def PrintDna(self):
		if len(self.sequence) == 0:
			print("Error : DNA length = 0 ==>  You must generate a DNA sequence first !!!")
		else:
			print(self.sequence)

#Dna1 = DNA(10)
#Dna1.DnaGen()
#Dna1.PrintDna()

#Dna2 = DNA(0)
#Dna2.DnaGen()
#Dna2.PrintDna()

#Dna3 = DNA(20)
#Dna3.DnaGen()
#Dna3.PrintDna()



