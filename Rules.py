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
import time

from random import shuffle

class Rules():

	def __init__(self):
	
		def CreatePlayers(num):
			for i in range(0, num):
				self.players.append(Player(order = i, Strat = "risky"))
				
		def loadProperties():
			properties = open("properties.txt")
			for line in properties:
				params = line.split(";")
				self.tiles[int(params[2])] = (Property(params[0], params[1], int(params[2]), int(params[3]), [int(s) for s in params[4].split(",")], int(params[5]), params[6], int(params[7])))
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
		self.Cards = {}
		self.tiles = {}
	
		CreatePlayers(self.numPlayers)
		loadProperties()
		
		#load cards
		loadCards = ImportCards()
		self.Cards = loadCards.loadCards()
		#shuffle card piles
		shuffle(self.Cards["chance"])
		shuffle(self.Cards["chest"])
		
	def getTiles(self):
		return self.tiles
		
	def getBoard(self):
		return self.board
		
	def getPlayer(self, player):
		return self.players[player]
	
	def getCard(self, card):
		return self.Cards[card]


	def runGame(self, api, gui):
		
		def DecideTurnOrder(players, dice): #decide a initial player based on dice rolls
			first = 0
			highestRoll = 0
			for i in range(0, players):
				roll = dice.RollDice()
				if roll > highestRoll:
					highestRoll = roll
					first = i
			return first
		def isGameOver(players): #check if the game is finished
			bankrupt = 0
			for i in range(0, len(players)):
				if players[i].GetCash() < 0:
					bankrupt += 1
					
			if bankrupt == len(players) - 1:
				return True
			else:
				return False
		
		def nextPlayer(player):	#move to next players turn
			player = self.players.index(player) + 1
			if player == len(self.players):
				player = 0
			return player
			
		def	drawCard(type, player, api):#draw a card of correct type
			card = self.Cards[type][0]
			del	self.Cards[type][0]
			keep = api.playCard(card, player)
			if not keep:
				self.Cards[type].append(card)
				
		def canAfford(player, cost):	
			if (cost + api.getHighestRent(player)) < player.GetCash():
				return True
			else:
				return False
		
		def isBuyingHouses(player, api): #decide whether the player is buying houses and for which property
			playersProperties = player.GetOwnedPropertys()
			lowestCost = 9999
			cheapestHouseProperty = ""
			for property in playersProperties:
				if api.inMonopoly(property, player):
					if property.GetHouseCost() < lowestCost and property.GetNumHouses() < 5 and api.checkIfEvenBuild(property, player):
						lowestCost = property.GetHouseCost()
						cheapestHouseProperty = property
			if canAfford(player, lowestCost) :
				return [True, cheapestHouseProperty]
			else:
				return [False]
			
		def sellForCash(player, api):
			properties = player.GetOwnedPropertys()
			lowestCost = 9999
			selling = ""
			sellImprovments = False
			
			for property in properties:
				if (property.GetBuyValue() < lowestCost) and (not(api.inMonopoly(property, player))) and not(property.GetIsMorgaged()):
					lowestCost = property.GetBuyValue()
					selling = property
					
			if lowestCost == 9999:
				for property in properties:
					if (property.GetBuyValue() < lowestCost) and (not(property.GetIsMorgaged())) and (api.getNumHouses(player, property.GetGroup()) == 0):
						lowestCost = property.GetBuyValue()
						selling = property
						
			if lowestCost == 9999:
				for property in properties:
					if (property.GetHouseCost() < lowestCost) and not(property.GetIsMorgaged()) and  property.GetNumHouses() > 0:
						sellImprovments = True
						lowestCost = property.GetHouseCost()
						selling = property
			
			if sellImprovments == True:
				api.sellHouses(player, selling)
			elif sellImprovments == False:
				api.morgageProperty(player, selling)
				
		currentPlayer = self.players[DecideTurnOrder(len(self.players), self.dice)]#decide first player
		
		while not(isGameOver(self.players)):#while the game is not over
		
			if api.isBankrupt(currentPlayer):#if player is bankkrupt move to next player
				playerNum = nextPlayer(currentPlayer)
				currentPlayer = self.players[playerNum]
			else:
			
				if currentPlayer.GetJailTurns() > 0: #if in jail
					currentPlayer.decJailTurns() #reduce jail turns
					api.tryOutOfJail(currentPlayer, self.dice) #attempt to get out of jail using dice roll
					
				else:
				
					roll = api.rollDice(currentPlayer, self.dice) # roll dice
					oldTile = currentPlayer.GetBoardPos() #store previous tile 
					api.movePlayer(currentPlayer,roll) #move player
					if api.checkIfPassGo(currentPlayer, oldTile): #check if passed GO and pay amount
						api.deductCash(currentPlayer, self.tiles[0].GetTax())
					currentTile = self.tiles[currentPlayer.GetBoardPos()]
					
					#thge tile is a ownavle property tile
					if currentTile.GetType() in ["standard", "utility", "station"]:
						#is the property owned
						if currentTile.GetOwner() == "": #no
							if canAfford(currentPlayer, currentTile.GetBuyValue()):#can afford the property
								api.buyProperty(currentPlayer, currentTile)#buy property
						else: #yes
							#pay the rent to the owner
							if currentTile.GetOwner().GetJailTurns() == 0:#if tile owner is not in jail
								if not(currentTile.GetType() == "utility"):
									if currentPlayer.GetCash() > currentTile.GetRent():#if can afford rent
										api.payRent(currentPlayer, currentTile.GetOwner(), currentTile)
									else:	
										bankrupt = False
										while currentPlayer.GetCash() < currentTile.GetRent() and bankrupt == False:#while the player doesnt have enough money and is not bankrupt
											sellForCash(currentPlayer, api)
											bankrupt = api.isBankrupt(currentPlayer, currentTile.GetRent())
										if bankrupt == True:# if bankrupt give all properties and cash to bankrupting player
											currentTile.GetOwner().GetOwnedPropertys().append(currentPlayer.GetOwnedPropertys())
											api.giveCash(currentTile.GetOwner(), currentPlayer.GetCash())
											api.deductCash(currentPlayer, currentPlayer.GetCash())
								else:
									if currentPlayer.GetCash() > (currentTile.GetRent() * roll):#if can afford rent
										api.payRent(currentPlayer, currentTile.GetOwner(), currentTile, roll)
									else:	
										bankrupt = False
										while currentPlayer.GetCash() < (currentTile.GetRent()  * roll) and bankrupt == False:#while the player doesnt have enough money and is not bankrupt
											sellForCash(currentPlayer, api)
											bankrupt = api.isBankrupt(currentPlayer, currentTile.GetRent() * roll)
										if bankrupt == True:# if bankrupt give all properties and cash to bankrupting player
											currentTile.GetOwner().GetOwnedPropertys().append(currentPlayer.GetOwnedPropertys())
											api.giveCash(currentTile.GetOwner(), currentPlayer.GetCash())
											api.deductCash(currentPlayer, currentPlayer.GetCash())
								
					#the tile is a card tile			
					elif currentTile.GetType() in ["chance", "chest"]:
						drawCard(currentTile.GetType(), currentPlayer, api)
						
					#tile is a tax tile	
					elif currentTile.GetType() == "tax":
						api.deductCash(currentPlayer, currentTile.GetTax())
					
					elif currentTile.GetType() in ["free", "jail"]:
						pass
					elif currentTile.GetType() == "toJail":
						api.sendToJail(currentPlayer)
						
					if not(currentPlayer.GetJailTurns() > 0): #if not in jail
						if api.hasMonopoly(currentPlayer):
							#buy houses
							buyingHouses = isBuyingHouses(currentPlayer)
							while buyingHouses[0]:
								api.improveProperty(currentPlayer, buyingHouses[1])
								buyingHouses = isBuyingHouses(currentPlayer)
					
					gui.update(self.players)
					time.sleep(1)
					currentPlayer = self.players[nextPlayer(currentPlayer)]
if __name__ == "__main__":
	game = Rules()
	visuals = MonopolyGUI()
	visuals.load(game.getBoard().GetDimentions(), game.getTiles())
	api = API(game.getTiles(), game.getBoard())
	game.runGame(api, visuals)
