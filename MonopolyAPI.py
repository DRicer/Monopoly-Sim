import Dice
import Board
import Player
import Property
import SpecialProperty
import Tile
import Card

class API():

	def __init__(self, tiles, board):
		self.tiles = tiles
		self.board = board
		self.cardApi = {"movePlayer" : self.movePlayer, "rollDice": self.rollDice, "sendToJail": self.sendToJail, "getOutOfJail": self.getOutOfJail, "checkIfPassGo": self.checkIfPassGo, "buyProperty": self.buyProperty,
		"payRent" : self.payRent, "deductCash": self.deductCash, "giveCash": self.giveCash, "improveProperty": self.improveProperty, "sellHouses": self.sellHouses, "morgageProperty": self.morgageProperty,
		"checkEvenBuild": self.checkEvenBuild, "sendTo": self.sendTo, "findNearest": self.findNearest}
		
	def movePlayer(self, player, move):
		player.SetBoardPos(player.GetBoardPos() + move)
		maxTile = len(self.tiles)
		if player.GetBoardPos() >= maxTile:
			player.SetBoardPos(player.getBoardPos - maxTile)
			
	def rollDice(self, player, dice):
		roll = dice.RollDice()
		if dice.GetDoublesCount() == dice.GetJailRoll():
			sendToJail(player)
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
		oldDoubles = dice
		if dice.GetDoublesCount() == 1:
			player.SetJailTurns(0)
			dice.SetDoublesCount(0)
			
	def checkIfPassGo(self, player, oldTile):
		if player.GetBoardPos() < oldTile:
			return True
		else:
			return False
	
	def buyProperty(self, player, property):
		player.LoseCash(property.GetBuyValue())
		player.AddProperty(property)
		property.SetOwner(player)
		
	def payRent(self, paying, recieving, property, multiplier = 1):
	
		if property.GetType() == "standard":
			paying.LoseCash(property.GetRent() * multiplier)
			recieving.GainCash(property.GetRent() * multiplier)
			
		else:
			num = 0
			
			for tile in recieving.GetOwnedPropertys():
			
				if tile.GetType() == property.GetType():
					num += 1
			
			if property.GetType() == "station":
				paying.LoseCash(property.GetRent(2**(num-1) * multiplier))
				recieving.GainCash(property.GetRent(2**(num-1) * multiplier))
				
			elif property.GetType() == "utility":
				paying.LoseCash(property.GetRent(num) * multiplier)
				recieving.GainCash(property.GetRent(num) * multiplier)
	
	def deductCash(self, player, amount):
		player.LoseCash(amount)
	
	def giveCash(self, player, amount):
		player.GainCash(amount)
	
	def improveProperty(self, player, property):
		property.SetNumHouses(property.GetNumHouses() + 1)
		player.LoseCash(property.GetHouseCost())
	
	def sellHouses(self, player, property):
		property.SetNumHouses(property.GetNumHouses() - 1)
		player.GainCash(property.GetHouseCost())
		
	def morgageProperty(self, player, property):
		property.SetIsMorgaged(true)
		player.GainCash(property.GetBuyValue() * board.GetMorgagePercent())
		
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
	def getHighestRent(self, player):
		highest = 0
		for property in tiles():
			if not(property.GetOwner() == player):
				if property.GetRent() > highest:
					highest = property.GetRent()
					
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
			
			for param in params:
			
				if "player" in param:
				
					if "self" in param:
						params[params.index(param)] = player
						
				elif "property" in param:
				
					params[params.index(param)] = findProperty(param[param.index("{") + 1:-1])
					
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
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					