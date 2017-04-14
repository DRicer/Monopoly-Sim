import Dice
import Board
import Player
import Property
import SpecialProperty
import Tile

class API():

	def __init__(self, tiles, board):
		self.tiles = tiles
		self.board = board
		
	def movePlayer(self, player, move):
		player.MovePlayer(move)
		
	def rollDice(self, player, dice):
		roll = dice.RollDice()
		if dice.DoublesCount == dice.GetJailRoll:
			sendToJail(player)
	
	def sendToJail(self, player):
		player.SetJailTurns(3)
		for i in range(0, len(self.tiles)):
			if self.tiles[i].GetType() == "jail":
				player.SetBoardPos(self.tiles[i].GetBoardPos())
				break
	
	def getOutOfJail(self, player):
		player.SetJailTurns(0)
	
	def checkIfPassGo(self, player):
		pass
	
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
	
	def sellHouses(self, player, property):
		property.SetNumHouses(property.GetNumHouses() - 1)
	
	def morgageProperty(self, player, property):
		property.SetIsMorgaged(true)
		player.GainCash(property.GetBuyValue() * board.GetMorgagePercent())
		
	def checkEvenBuild(self, group):
		pass
	
	def sendTo(self, player, property):
		pass
	
	def findNearest(self, player, group):
		pass
	
	