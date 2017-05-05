

class Player():
	
	def __init__(self, order, Strat, startCash = 1500):
	
		if not isinstance(order, int):
			raise TypeError("rollOrder must be set to an integer")
			
		if not isinstance(startCash, int):
			raise TypeError("startCash must be set to an integer")
			
		if not isinstance(Strat, str):
			raise TypeError("Strategy must be set to a string")
			
		self.rollOrder = order
		self.Cash = startCash
		self.Strategy = Strat
		
		self.getOutOfJailCards = []
		self.ownedProperties = []
		self.boardPos = 0
		self.jailTurns = 0
		self.bankrupt = False
	
	def GetIsBankrupt(self):
		return self.bankrupt
		
	def SetIsBankrupt(self, new):
		self.bankrupt = new
	
	def GetRollOrder(self):
		return self.rollOrder
		
	def SetRollOrder(self, newOrder):
		self.rollOrder = newOrder
		
	def AddProperty(self, property):
		self.ownedProperties.append(property)
		
	def RemoveProperty(self, property):
		self.ownedProperties.remove(property)
		
	def GetOwnedPropertys(self):
		return self.ownedProperties
	
	def SetOwnedPropertys(self, new):
		if not isinstance(new, list):
			raise TypeError("propertys must be set to a list")
	
		self.ownedProperties = new
		#
	def GetCash(self):
		return self.Cash
		
	def GainCash(self, amount):
		self.Cash += amount
	
	def LoseCash(self, amount):
		self.Cash -= amount
		
	def SetCash(self, amount):
		self.Cash = amount
	
	def SetBoardPos(self, pos):
		if not isinstance(pos, int):
			raise TypeError("BoardPos must be set to an integer")
		self.boardPos = pos
		
	def GetBoardPos(self):
		return self.boardPos
		
		
	def SetStrategy(self, strat):
		self.Strategy = strat
		
	def GetStrategy(self):
		return self.Strategy
		
	def SetJailTurns(self, turns):
		self.jailTurns = turns
		
	def GetJailTurns(self):
		return self.jailTurns
		
	def decJailTurns(self):
		self.jailTurns -= 1
		
	def AddGetOutOFJail(self, card):
		self.getOutOfJailCards.append(card)
	
	def HasGetOutOFJail(self):
		if self.getOutOfJailCards:
			return True
		
	def UseGetOutOFJail(self):
		self.jailTurns = 0
		card = self.getOutOfJailCards[0]
		del self.getOutOfJailCards[0]
		return card
	