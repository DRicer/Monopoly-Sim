

class Player():
	
	def __init__(self, order, startCash = 1500, Strat):
	
		if not isinstance(order, int):
			raise TypeError("rollOrder must be set to an integer")
			
		if not isinstance(startCash, int):
			raise TypeError("startCash must be set to an integer")
			
		if not isinstance(Strat, str):
			raise TypeError("Strategy must be set to a string")
			
		self.rollOrder = order
		self.Cash = startCash
		self.Strategy = Strat
		
		self.ownedProperties = []
		self.boardPos = 0
		self.jailTurns = 0
	
	def GetRollOrder():
		return rollOrder
		
	def SetRollOrder(newOrder):
		rollOrder = newOrder
		
	def AddProperty(property):
		ownedProperties.append(property)
		
	def RemoveProperty(property):
		ownedProperties.remove(property)
		
	def GetOwnedPropertys():
		return ownedProperties
		
	def GainCash(amount):
		Cash += amount
	
	def LoseCash(amount):
		Cash -= amount
		
	def SetCash(amount):
		Cash = amount
	
	def SetBoardPos(pos):
		boardPos = pos
		
	def GetBoardPos(pos):
		return boardPos
		
	def MovePlayer(spaces):
		boardPos += spaces
		
	def SetStrategy(strat):
		Strategy = strat
		
	def GetStrategy():
		return Strategy
		
	def SetJailturns(turns):
		jailTurns = turns
		
	def GetJailTurns():
		return jailTurns
		
	def decJailTurns():
		jailTurns -= 1
		
	