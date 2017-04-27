from Dice import Dice
from Board import Board
from Player import Player
from Property import Property
from SpecialProperty import SpecialProperty
from TaxTile import TaxTile
from Tile import Tile
from MonopolyAPI import API
from ImportCards import ImportCards
from MonopolyGUI import MonopolyGUI

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
		self.Cards = []
		self.tiles = {}
	
		CreatePlayers(self.numPlayers)
		loadProperties()
		loadCards = ImportCards()
		self.Cards = loadCards.loadCards()
		
	def getTiles(self):
		return self.tiles
		
	def getBoard(self):
		return self.board
		
	def getPlayer(self, player):
		return self.players[player]
	
	def getCard(self, card):
		return self.Cards[card]


	def RunGame(self, api):
		
		def DecideTurnOrder(players, dice):
			first = 0
			highestRoll == 0
			for i in range(0, players):
				roll = dice.Rolldice()
				if roll > highestRoll:
					highestRoll = roll
					first = i
			return first
		def isGameOver(players):
			bankrupt = 0
			for i in range(0, len(players))
				if players[i].GetCash() < 0
					bankrupt += 1
					
			if bankrupt == len(players) - 1:
				return True
			else:
				return False
		
		def nextPlayer(Player):	
			Player += 1
				if Player == len(players):
					Player = 0
			return Player
			
		
		currentPlayer = DecideTurnOrder(len(self.players), self.dice)
		while not(isGameOver(self.players)):
			if self.players[currentPlayer].GetCash() < 0:
				currentPlayer = nextPlayer(currentPlayer)
			
			else:
				if self.players[currentPlayer].GetJailTurns() > 0: #if in jail
					self.players[currentPlayer].decJailTurns() #reduce jail turns
					api.tryOutOfJail(self.players[currentPlayer], self.dice) #attempt to get out of jail using dice roll
				else:
					api.movePlayer(self.players[currentPlayer], api.rollDice(self.players[currentPlayer], self.dice))
					
		
		
		
		
if __name__ == "__main__":
	game = Rules()
	visuals = MonopolyGUI()
	visuals.load(game.getBoard().GetDimentions(), game.getTiles())
	api = API(game.getTiles(), game.getBoard())
	
