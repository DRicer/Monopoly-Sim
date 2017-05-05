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
		self.log = []
		self.turnCount = 0
		
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
	
	def getPlayers(self):
		return self.players
	
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
				if players[i].GetIsBankrupt():
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
			
			self.log.append("player " + str(currentPlayer.GetRollOrder()) + "'s card is:  '" + card.GetText() + "'")
			print("player " + str(currentPlayer.GetRollOrder()) + "'s card is:  '" + card.GetText() + "'")
			
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
					if property.GetHouseCost() < lowestCost and property.GetNumHouses() < 5 and api.checkIfEvenBuild(property, player) and self.board.GetAvailableHouses() > 0:
						lowestCost = property.GetHouseCost()
						cheapestHouseProperty = property
			if canAfford(player, lowestCost) and not(cheapestHouseProperty == "") :
				return [True, cheapestHouseProperty]
			else:
				return [False]
			
		def sellForCash(player, api):
			properties = player.GetOwnedPropertys()
			lowestCost = 9999
			selling = ""
			sellImprovments = False
			
			for property in properties:
				if (property.GetBuyValue() < lowestCost) and property.GetType() == "utility" and not(property.GetIsMorgaged()):
					lowestCost = property.GetBuyValue()
					selling = property
					
			if lowestCost == 9999:	
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
					if hasattr(property, "GetHouseCost"):
						if (property.GetHouseCost() < lowestCost) and not(property.GetIsMorgaged()) and  property.GetNumHouses() > 0 and api.checkIfEvenBuild(property, player, False):
							sellImprovments = True
							lowestCost = property.GetHouseCost()
							selling = property
			
			if not selling == "":
				if sellImprovments == True:
					api.sellHouses(player, selling)
					self.log.append("player " + str(player.GetRollOrder()) + " sells imporvements on " + str(selling.GetName()))
					print("player " + str(player.GetRollOrder()) + " sells imporvements on " + str(selling.GetName()))
					
				elif sellImprovments == False:
					api.morgageProperty(player, selling)
					self.log.append("player " + str(player.GetRollOrder()) + " morgages " + str(selling.GetName()))
					print("player " + str(player.GetRollOrder()) + " morgages " + str(selling.GetName()))
				
		currentPlayer = self.players[DecideTurnOrder(len(self.players), self.dice)]#decide first player
		
		while not(isGameOver(self.players)):#while the game is not over
		
			if currentPlayer.GetIsBankrupt():#if player is bankkrupt move to next player
				playerNum = nextPlayer(currentPlayer)
				currentPlayer = self.players[playerNum]
			else:
			
				if currentPlayer.GetJailTurns() > 0 and not currentPlayer.HasGetOutOFJail(): #if in jail
						
						currentPlayer.decJailTurns() #reduce jail turns
						self.log.append("player " + str(currentPlayer.GetRollOrder()) + " has " + str(currentPlayer.GetJailTurns()) + " left in jail")
						print("player " + str(currentPlayer.GetRollOrder()) + " has " + str(currentPlayer.GetJailTurns()) + " left in jail")
						
						if canAfford(currentPlayer, self.board.GetBail()):#can player afford bail
							api.deductCash(currentPlayer, self.board.GetBail())
							api.getOutOfJail(currentPlayer)
							self.log.append("player " + str(currentPlayer.GetRollOrder()) + " pays bail")
							print("player " + str(currentPlayer.GetRollOrder()) + " pays bail")
						
						elif api.tryOutOfJail(currentPlayer, self.dice): #attempt to get out of jail using dice roll
							self.log.append("player " + str(currentPlayer.GetRollOrder()) + " gets out of jail with a roll")
							print("player " + str(currentPlayer.GetRollOrder()) + " gets out of jail with a roll")
				else:
					if currentPlayer.HasGetOutOFJail():
						jailCard = currentPlayer.UseGetOutOFJail()
						self.Cards[jailCard.GetType()].append(jailCard)
					
					roll = api.rollDice(currentPlayer, self.dice)# roll dice
					oldTile = currentPlayer.GetBoardPos() #store previous tile 
					api.movePlayer(currentPlayer,roll) #move player
						
					self.log.append("player " + str(currentPlayer.GetRollOrder()) + " moves from " + str(self.tiles[oldTile].GetName()) + " to " + str(self.tiles[currentPlayer.GetBoardPos()].GetName()))
					print("player " + str(currentPlayer.GetRollOrder()) + " moves from " + str(self.tiles[oldTile].GetName()) + " to " + str(self.tiles[currentPlayer.GetBoardPos()].GetName()))
					if api.checkIfPassGo(currentPlayer, self.tiles[oldTile]): #check if passed GO and pay amount
						api.deductCash(currentPlayer, self.tiles[0].GetTax())
						self.log.append("player" + str(currentPlayer.GetRollOrder()) + "collects £200 for passing GO")
						print("player " + str(currentPlayer.GetRollOrder()) + " collects £200 for passing GO")
					currentTile = self.tiles[currentPlayer.GetBoardPos()]
					
					#the tile is a card tile			
					if currentTile.GetType() in ["chance", "chest"]:
						self.log.append("player " + str(currentPlayer.GetRollOrder()) + " draws a " + str(currentTile.GetType()))
						print("player " + str(currentPlayer.GetRollOrder()) + " draws a " + str(currentTile.GetType()))
						drawCard(currentTile.GetType(), currentPlayer, api)
						bankrupt = False
						while currentPlayer.GetCash() < 0 and bankrupt == False:#while the player doesnt have enough money and is not bankrupt
							sellForCash(currentPlayer, api)
							bankrupt = api.isBankrupt(currentPlayer)
						if bankrupt == True:# if bankrupt give all properties and cash to bank
							currentPlayer.SetIsBankrupt(True)
							api.deductCash(currentPlayer, currentPlayer.GetCash())
							for property in currentPlayer.GetOwnedPropertys():
								property.SetOwner("")
								currentPlayer.SetOwnedPropertys([])
					
					gui.update(self.players, oldTile)
					oldTile = currentTile.GetBoardPos() 
					currentTile = self.tiles[currentPlayer.GetBoardPos()]
					
					#the tile is an ownable property tile
					if currentTile.GetType() in ["standard", "utility", "station"]:
						#is the property owned
						if currentTile.GetOwner() == "": #no
							if canAfford(currentPlayer, currentTile.GetBuyValue()):#can afford the property
								api.buyProperty(currentPlayer, currentTile)#buy property
								self.log.append("player " + str(currentPlayer.GetRollOrder()) + " buys " + str(currentTile.GetName()))
								print("player " + str(currentPlayer.GetRollOrder()) + " buys " + str(currentTile.GetName()))
						elif currentTile.GetOwner().GetJailTurns() == 0 and currentTile.GetIsMorgaged() == False and not(currentPlayer == currentTile.GetOwner()):#if tile owner is not in jail
							if not(currentTile.GetType() == "utility"):
								if currentPlayer.GetCash() > currentTile.GetRent():#if can afford rent
									api.payRent(currentPlayer, currentTile.GetOwner(), currentTile)
									self.log.append("player " + str(currentPlayer.GetRollOrder()) + " pays rent of " + str(currentTile.GetRent()) + " to player " + str(currentTile.GetOwner().GetRollOrder()))
									print("player " + str(currentPlayer.GetRollOrder()) + " pays rent of " + str(currentTile.GetRent()) + " to player " + str(currentTile.GetOwner().GetRollOrder()))
								else:	
									bankrupt = False
									while currentPlayer.GetCash() < currentTile.GetRent() and bankrupt == False:#while the player doesnt have enough money and is not bankrupt
										sellForCash(currentPlayer, api)
										bankrupt = api.isBankrupt(currentPlayer, currentTile.GetRent())
									if bankrupt == True:# if bankrupt give all properties and cash to bankrupting player
										currentPlayer.SetIsBankrupt(True)
										self.log.append("player " + str(currentPlayer.GetRollOrder()) + " goes bankrupt to " + str(currentTile.GetOwner().GetRollOrder()))
										print("player " + str(currentPlayer.GetRollOrder()) + " goes bankrupt to " + str(currentTile.GetOwner().GetRollOrder()))
										currentTile.GetOwner().SetOwnedPropertys(currentTile.GetOwner().GetOwnedPropertys() + currentPlayer.GetOwnedPropertys())
										for property in currentPlayer.GetOwnedPropertys():
											property.SetOwner("")
										currentPlayer.SetOwnedPropertys([])
										api.giveCash(currentTile.GetOwner(), currentPlayer.GetCash())
										api.deductCash(currentPlayer, currentPlayer.GetCash())
									else:
										api.payRent(currentPlayer, currentTile.GetOwner(), currentTile)
										self.log.append("player " + str(currentPlayer.GetRollOrder()) + " pays rent of " + str(currentTile.GetRent()) + " to player " + str(currentTile.GetOwner().GetRollOrder()))
									print("player " + str(currentPlayer.GetRollOrder()) + " pays rent of " + str(currentTile.GetRent()) + " to player " + str(currentTile.GetOwner().GetRollOrder()))
							else:
								if currentPlayer.GetCash() > (currentTile.GetRent() * roll):#if can afford rent
									api.payRent(currentPlayer, currentTile.GetOwner(), currentTile, roll)
									self.log.append("player " + str(currentPlayer.GetRollOrder()) + " pays rent of " + str(currentTile.GetRent() * roll) + " to player " + str(currentTile.GetOwner().GetRollOrder()))
									print("player " + str(currentPlayer.GetRollOrder()) + " pays rent of " + str(currentTile.GetRent() * roll) + " to player " + str(currentTile.GetOwner().GetRollOrder()))
								else:	
									bankrupt = False
									while currentPlayer.GetCash() < (currentTile.GetRent()  * roll) and bankrupt == False:#while the player doesnt have enough money and is not bankrupt
										sellForCash(currentPlayer, api)
										bankrupt = api.isBankrupt(currentPlayer, currentTile.GetRent() * roll)
									if bankrupt == True:# if bankrupt give all properties and cash to bankrupting player
										currentPlayer.SetIsBankrupt(True)
										self.log.append("player " + str(currentPlayer.GetRollOrder()) + " goes bankrupt to " + str(currentTile.GetOwner().GetRollOrder()))
										print("player " + str(currentPlayer.GetRollOrder()) + " goes bankrupt to " + str(currentTile.GetOwner().GetRollOrder()))
										currentTile.GetOwner().SetOwnedPropertys(currentTile.GetOwner().GetOwnedPropertys() + currentPlayer.GetOwnedPropertys())
										for property in currentPlayer.GetOwnedPropertys():
											property.SetOwner(currentTile.GetOwner())
										currentPlayer.SetOwnedPropertys([])
										api.giveCash(currentTile.GetOwner(), currentPlayer.GetCash())
										api.deductCash(currentPlayer, currentPlayer.GetCash())
									else:
										api.payRent(currentPlayer, currentTile.GetOwner(), currentTile, roll)
									self.log.append("player " + str(currentPlayer.GetRollOrder()) + " pays rent of " + str(currentTile.GetRent() * roll) + " to player " + str(currentTile.GetOwner().GetRollOrder()))
									print("player " + str(currentPlayer.GetRollOrder()) + " pays rent of " + str(currentTile.GetRent() * roll) + " to player " + str(currentTile.GetOwner().GetRollOrder()))
							
					
					#tile is a tax tile	
					elif currentTile.GetType() == "tax":
						bankrupt = False
						while currentPlayer.GetCash() < currentTile.GetTax() and bankrupt == False:#while the player doesnt have enough money and is not bankrupt
							sellForCash(currentPlayer, api)
							bankrupt = api.isBankrupt(currentPlayer, currentTile.GetTax())
						if bankrupt == True:# if bankrupt give all properties and cash to bank
							currentPlayer.SetIsBankrupt(True)
							api.deductCash(currentPlayer, currentPlayer.GetCash())
							for property in currentPlayer.GetOwnedPropertys():
								property.SetOwner("")
							currentPlayer.SetOwnedPropertys([])
						else:
							api.deductCash(currentPlayer, currentTile.GetTax())
							self.log.append("player " + str(currentPlayer.GetRollOrder()) + " pays tax: " + str(currentTile.GetTax()))
							print("player " + str(currentPlayer.GetRollOrder()) + " pays tax: " + str(currentTile.GetTax()))
					
					elif currentTile.GetType() in ["free", "jail"]:
						pass
					elif currentTile.GetType() == "toJail":
						api.sendToJail(currentPlayer)
						self.log.append("player " + str(currentPlayer.GetRollOrder()) + " is sent to jail ")
						print("player " + str(currentPlayer.GetRollOrder()) + " is sent to jail ")
						
					if not(currentPlayer.GetJailTurns() > 0): #if not in jail
						if api.hasMonopoly(currentPlayer):
							#buy houses
							buyingHouses = isBuyingHouses(currentPlayer, api)
							while buyingHouses[0]:
								api.improveProperty(currentPlayer, buyingHouses[1])
								self.log.append("player " + str(currentPlayer.GetRollOrder()) + " improves " + str(buyingHouses[1].GetName()))
								print("player " + str(currentPlayer.GetRollOrder()) + " improves " + str(buyingHouses[1].GetName()))
								buyingHouses = isBuyingHouses(currentPlayer, api)
						#unmorgage
						for property in currentPlayer.GetOwnedPropertys():
							if property.GetIsMorgaged():
								if canAfford(currentPlayer, (property.GetBuyValue() * self.board.GetMorgagePercent()) * self.board.GetMorgageInterest()):
									api.unMorgageProperty(currentPlayer, property)
									self.log.append("player " + str(currentPlayer.GetRollOrder()) + " unmorgages " + str(property.GetName()))
									print("player " + str(currentPlayer.GetRollOrder()) + " unmorgages " + str(property.GetName()))
				print()	
				gui.update(self.players, oldTile)
				time.sleep(1)
				self.turnCount += 1
				if not self.dice.GetDoublesCount() > 0:						
					currentPlayer = self.players[nextPlayer(currentPlayer)]
		
		WinningPlayer = ""
		for player in self.players:
			if not player.GetIsBankrupt():
				WinningPlayer = self.players.index(player)
		print("The Winner is: Player " + str(WinningPlayer))
		logFile = open("log.txt", "w")
		for item in self.log:
			logFile.write("%s\n" % item)
		for tile in self.tiles:
			if hasattr(tile, "GetEarnings"):
				logFile.write("%s\n" % (self.tiles[tile].GetName() + "'s earnings: " + str(self.tiles[tile].GetEarnings())))
		logFile.write("%s\n" % ("Total Turns: " + str(self.turnCount)))	
		
if __name__ == "__main__":
	game = Rules()
	visuals = MonopolyGUI()
	visuals.load(game.getBoard().GetDimentions(), game.getTiles(), game.getPlayer(0).GetCash())
	api = API(game.getTiles(), game.getBoard(), game.getPlayers())
	game.runGame(api, visuals)
