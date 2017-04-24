from Tile import Tile

class SpecialProperty(Tile):


	def __init__(self, name, type, boardPos, buyValue, multipliers, group):
	
		Tile.__init__(self, name, type, boardPos)
		
		if not isinstance(name, str):
			raise TypeError("name must be set to a string")
		self.name = name
		
		if not isinstance(buyValue, int):
			raise TypeError("buyValue must be set to an int")
		self.buyValue = buyValue
		
		if not isinstance(multipliers, list):
			raise TypeError("multipliers must be set to an list")
		self.multipliers = multipliers
		
		if not isinstance(group, str):
			raise TypeError("group must be set to a string")
		self.group = group
		
		self.isMorgaged = False
		self.owner = ""
	
		
	def SetBuyValue(self, new):
		if not isinstance(new, int):
			raise TypeError("buyValue must be set to an int")
			
		self.buyValue = new	
	
	def GetBuyValue(self):
		return self.buyValue
		
	def SetMultipliers(self, new):
		if not isinstance(new, list):
			raise TypeError("multipliers must be set to an list")
			
		self.multipliers = new
		
	def GetMultipliers(self):
		return self.multipliers
		
	def GetRent(self, num):
		return self.multipliers[num]
		
	def SetIsMorgaged(self, new):
		if not isinstance(new, bool):
			raise TypeError("isMorgaged must be set to a boolean")
			
		self.isMorgaged = new
		
	def GetIsMorgaged(self):
		return self.isMorgaged
		
	def SetGroup(self):
		if not isinstance(new, str):
			raise TypeError("group must be set to a string")
			
		self.group = new
		
	def GetGroup(self):
		return self.group
		
	def SetOwner(self, new):
		if not isinstance(new, Player):
			raise TypeError("owner must be set to a Player")
		
		self.owner = new
			
	def GetOwner(self):
		return self.owner