import random

class DNA():
	"""This module creates a dna sequence """

	acid = ['A','C','G','T']
	sequence = ''

	
	def __init__(self, DNA_length):
		self.DNA_length = DNA_length

	def DnaGen(self):
		""" This function creates a sequence of Dna based on a given length"""
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
		""" This function print the sequence of Dna"""

		if len(self.sequence) == 0:
			print("Error : DNA length = 0 ==>  You must generate a DNA sequence first !!!")
		else:
			print(self.sequence)
