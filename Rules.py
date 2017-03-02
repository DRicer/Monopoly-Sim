import Dice
import Board
import Player
import Property
import SpecialProperty
import Tile

class Rules():

	def __init__(self):
		self.dice = Dice()
		self.board = Board()
		self.numPlayers = 4
		self.players = []
		self.propeties = []
		CreatePlayers(numPlayers)
	
	
	def CreatePlayers(num):
		for i in range(0, num):
			players.append(Player(order = i, strat = "risky"))
			
	def loadProperties():
	
	