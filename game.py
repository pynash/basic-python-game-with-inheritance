#######################################################
#	memoriza secuencia de numeros 		      #
#######################################################
import os, time

class Game(object):
	def __init__(self, level):
		self.level = level
		self.block_number = self.randomize()

	def memoriza(self):
		os.system("clear")
		if self.level == 1:
			print "Recuerda la secuencia de los siguientes numeros, para despues escribir segun los recuerdes"
			for i in range(len(self.block_number)):
				print self.block_number[i]
				time.sleep(3)
				os.system("clear")
		elif (self.level == 2):
			for i in range(len(self.block_number)):
				print "Recuerda la secuencia de los siguientes numeros, para despues escribir segun los recuerdes"
				print self.block_number[i]
				time.sleep(3)
				os.system("clear")
	def Leer(self):
		self.puntaje = 0
		for i in range(len(self.block_number)):
			num1 = int(input("\nDigita Numero de la secuencia: "))
			if num1 == self.block_number[i]:
				print "es correcto, has ganado 5 puntos"
				self.puntaje += 5
			else:
				print "lo siento, no has acertado!"
			
	def final(self):
		return "tu puntaje es de: " + str(self.puntaje) 
		
	def randomize(self):
		import random
		block_number = []
		if self.level == 1:
			for i in range(5):
				num = random.randint(1, 20)
				block_number.append(num)
		elif self.level == 2:
			for i in range(10):
				num = random.randint(9, 50)
				block_number.append(num)
		return block_number
