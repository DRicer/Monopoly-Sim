import Dice
import Board
import Player
import Property
import SpecialProperty
import Tile
import Card

class API():

	def __init__(self, tiles, board, players):
		self.players = players
		self.tiles = tiles
		self.board = board
		self.cardApi = {"movePlayer" : self.movePlayer, "rollDice": self.rollDice, "sendToJail": self.sendToJail, "getOutOfJail": self.getOutOfJail, "checkIfPassGo": self.checkIfPassGo, "buyProperty": self.buyProperty,
		"payRent" : self.payRent, "deductCash": self.deductCash, "giveCash": self.giveCash, "improveProperty": self.improveProperty, "sellHouses": self.sellHouses, "morgageProperty": self.morgageProperty,
		"checkEvenBuild": self.checkEvenBuild, "sendTo": self.sendTo, "findNearest": self.findNearest, "birthdayCash" : self.birthdayCash, "makeRepairs" : self.makeRepairs}
		
	def movePlayer(self, player, move):
		player.SetBoardPos(player.GetBoardPos() + move)
		maxTile = len(self.tiles)
		if player.GetBoardPos() >= maxTile:
			player.SetBoardPos(player.GetBoardPos() - maxTile)
	
	def birthdayCash(self, player, amountPerPlayer):
		count  = 0
		for i in range(0, len(self.players)):
			self.players[i].LoseCash(amountPerPlayer)
			count += 1
		player.GainCash(amountPerPlayer * count)
		
	def rollDice(self, player, dice):
		roll = dice.RollDice()
		if dice.GetDoublesCount() == dice.GetJailonRoll():
			self.sendToJail(player)
			dice.SetDoublesCount(0)
		return roll
		
		
	def sendToJail(self, player):
		player.SetJailTurns(3)
		for i in range(0, len(self.tiles)):
			if self.tiles[i].GetType() == "jail":
				player.SetBoardPos(self.tiles[i].GetBoardPos())
				break
	
	def getOutOfJail(self, player):
		player.SetJailTurns(0)
		
	def tryOutOfJail(self, player, dice):
		roll = dice.RollDice()
		if dice.GetDoublesCount() == 1:
			dice.SetDoublesCount(0)
			return True
		else:
			return False
			
	def checkIfPassGo(self, player, oldTile):
		if player.GetBoardPos() < oldTile.GetBoardPos():
			return True
		else:
			return False
	
	def buyProperty(self, player, property):
		player.LoseCash(property.GetBuyValue())
		player.AddProperty(property)
		property.SetOwner(player)
		
	def payRent(self, paying, recieving, property, multiplier = 1):
	
			paying.LoseCash(property.GetRent() * multiplier)
			recieving.GainCash(property.GetRent() * multiplier)
			property.AddEarnings(property.GetRent() * multiplier)
	
	def deductCash(self, player, amount):
		player.LoseCash(amount)
	
	def giveCash(self, player, amount):
		player.GainCash(amount)
	
	def improveProperty(self, player, property):
		if self.board.GetAvailableHouses() > 0:
			property.SetNumHouses(property.GetNumHouses() + 1)
			player.LoseCash(property.GetHouseCost())
			property.DeductEarnings(property.GetHouseCost())
			self.board.DecAvailableHouses()
	
	def sellHouses(self, player, property):
		property.SetNumHouses(property.GetNumHouses() - 1)
		player.GainCash(property.GetHouseCost() * self.board.GetHouseSellPercent())
		property.AddEarnings(property.GetHouseCost() * self.board.GetHouseSellPercent())
		
	def morgageProperty(self, player, property):
		property.SetIsMorgaged(True)
		player.GainCash(property.GetBuyValue() * self.board.GetMorgagePercent())
		property.AddEarnings(property.GetBuyValue() * self.board.GetMorgagePercent())
		
	def unMorgageProperty(self, player, property):
		property.SetIsMorgaged(True)
		player.LoseCash((property.GetBuyValue() * self.board.GetMorgagePercent()) * self.board.GetMorgageInterest())
		property.AddEarnings((property.GetBuyValue() * self.board.GetMorgagePercent()) * self.board.GetMorgageInterest())
	
	def isBankrupt(self, player, toPay = 0):
		bankrupt = True
		ownedPropertys = player.GetOwnedPropertys()
		if ownedPropertys:
			for property in ownedPropertys:
				if property.GetIsMorgaged() == False:
					bankrupt = False
		if player.GetCash() - toPay >= 0:
				bankrupt = False
			
		return bankrupt
		
	def checkEvenBuild(self, group, player):
		owned = player.GetOwnedPropertys()
		groupProperties = []
		for property in owned:
			if property.GetGroup() == group:
				groupProperties.append(property)
		compariter = groupProperties[0].GetNumHouses()
		even = False
		for property in groupProperties:
			if ((property.GetNumHouses() - 1) == compariter) or ((property.GetNumHouses() + 1) == compariter):
				even = True
			else:
				even = False
		
		return even		
			
	def checkIfEvenBuild(self, buildProperty, player):
		owned = player.GetOwnedPropertys()
		groupProperties = []
		group = buildProperty.GetGroup()
		
		for property in owned:
			if property.GetGroup() == group:
				groupProperties.append(property)
				
		compariter = buildProperty.GetNumHouses() + 1
		even = False
		
		for property in groupProperties:
			if ((property.GetNumHouses() - 1) == compariter) or ((property.GetNumHouses() + 1) == compariter):
				even = True
			else:
				even = False	
		
		
		return even		

	def getNumHouses(self, player, group = "all"):#get the number of imporvements a player owns or in a specific group
		properties = player.GetOwnedPropertys()
		houses = 0
		if group == "all":
			for property in properties:
				houses += property.getNumHouses()
				
		else:
			for property in properties:
				if property.GetGroup() == group:
					houses += property.GetNumHouses()
		
		return houses
	
	def makeRepairs(self, player, perHouse, perHotel):
		properties = player.GetOwnedPropertys()
		for property in properties:
			if property.GetType() == "standard":
				if property.GetNumHouses == 5:
					player.LoseCash(perHotel)
				else:
					player.LoseCash(perHouse * property.GetNumHouses())
		
	def getHighestRent(self, player):
		highest = 0
		for property in self.tiles:
			if hasattr(self.tiles[property], "GetOwner") and not self.tiles[property].GetType() == "utility":
				if not(self.tiles[property].GetOwner() == player):
					if self.tiles[property].GetRent() > highest:
						highest = self.tiles[property].GetRent()
					
		return highest
		
		
	def sendTo(self, player, property):
		player.SetBoardPos(property.GetBoardPos())
	
	def findNearest(self, player, group):
	
		found = False
		pos = player.getBoardPos()
		maxTile = len(self.tiles)	
		while not found:
			pos += 1
			if pos == maxTile:
				pos = 0
				
			if tiles[pos].GetGroup() == group:
				found = true
				nearest = tiles[pos]
				
		return nearest
	
	def hasMonopoly(self, player): #check if the  player has at least one monopoly
		owned = player.GetOwnedPropertys()
		groups = {}
		for property in owned:
			if property.GetType() == "standard":
				if property.GetGroup() in groups:
					groups[property.GetGroup()] += 1
					if groups[property.GetGroup()] == property.GetInGroup():
						return True
				else:
					groups[property.GetGroup()] = 1
					if groups[property.GetGroup()] == property.GetInGroup():
						return True
		return False
		
	def inMonopoly(self, property, player):
		if property.GetType() == "standard":
			group = property.GetGroup()
			playerProps = player.GetOwnedPropertys()
			count = 0
			for prop in  playerProps:
				if prop.GetGroup() == group:
					count += 1
			if count == property.GetInGroup():
				return True
			else:
				return False
		else:
			return False
				
	def playCard(self, card, player):
	
		def findProperty(name):
			for i in range(0, len(self.tiles)):
				if self.tiles[i].GetName() == name:
					return self.tiles[i]
					break
	
		params = []
		cardActions = card.GetActions()

		for action in cardActions:
			params = cardActions[action].split(",")
			if "getOutOfJailFree" in action:
				player.AddGetOutOFJail
				return True
			for param in params:
			
				if "player" in param:
				
					if "self" in param:
						params[params.index(param)] = player
						
				elif "property" in param:
					if not ("current" in param):
						params[params.index(param)] = findProperty(param[param.index("{") + 1:-1])
					else:
						params[params.index(param)] = self.tiles[player.GetBoardPos()]
					
				elif "int" in param:
					
					params[params.index(param)] = int(param[param.index("{") + 1:-1])
				
					
			if len(params) == 1:
				self.cardApi[action](params[0])
			elif len(params) == 2:
				self.cardApi[action](params[0],params[1])	
			elif len(params) == 3:
				self.cardApi[action](params[0],params[1],params[2])			
			elif len(params) == 4:
				self.cardApi[action](params[0],params[1],params[2],params[3])			
					
		return False		
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					