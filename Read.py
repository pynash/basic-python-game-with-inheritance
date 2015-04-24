import os
from game import Game

class Level(Game):
	def __init__(self, nivel):
		Game.__init__(self, nivel)

	def run(self):
		Game.memoriza(self)
		#"raw_input('cuandes hayas memorizado! enter: ')
		Game.Leer(self)
		print Game.final(self)
			
