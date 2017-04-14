from Dice import Dice
from Board import Board
from Player import Player
from Property import Property
from SpecialProperty import SpecialProperty
from TaxTile import TaxTile
from Tile import Tile
from MonopolyAPI import API

class Rules():

	def __init__(self):
	
		def CreatePlayers(num):
			for i in range(0, num):
				self.players.append(Player(order = i, Strat = "risky"))
				
		def loadProperties():
			properties = open("properties.txt")
			for line in properties:
				params = line.split(";")
				self.tiles[int(params[2])] = (Property(params[0], params[1], int(params[2]), int(params[3]), [int(s) for s in params[4].split(",")], int(params[5]), params[6]))
			properties.close()
			
			specialProperties = open("otherProperties.txt")
			for line in specialProperties:
				params = line.split(";")
				self.tiles[int(params[2])] = (SpecialProperty(params[0], params[1], int(params[2]), int(params[3]), [int(s) for s in params[4].split(",")], params[5]))
			specialProperties.close()
			
			taxTiles = open("taxTiles.txt")
			for line in taxTiles:
				params = line.split(";")
				self.tiles[int(params[2])] = (TaxTile(params[0], params[1], int(params[2]), int(params[3])))
			taxTiles.close()
			
			otherTiles = open("otherTiles.txt")
			for line in otherTiles:
				params = line.split(";")
				self.tiles[int(params[2])] = (Tile(params[0], params[1], int(params[2])))
			otherTiles.close()
	
		self.dice = Dice()
		self.board = Board()
		self.numPlayers = 4
		self.players = []
		self.tiles = {}
	
		CreatePlayers(self.numPlayers)
		loadProperties()
		
	def getTiles(self):
		return self.tiles
		
	def getBoard(self):
		return self.board
		
	def getPlayer(self, player):
		return self.players[player]
		
if __name__ == "__main__":
	game = Rules()
	api = API(game.getTiles(), game.getBoard())
	api.sendToJail(game.getPlayer(1))
	print(game.getPlayer(1).GetJailTurns())
	print(game.getPlayer(1).GetBoardPos())