import Tile from Tile

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
	
		
	def SetBuyValue(new):
		if not isinstance(new, int):
			raise TypeError("buyValue must be set to an int")
			
		buyValue = new	
	
	def GetbuyValue():
		return buyValue
		
	def SetMultipliers(new):
		if not isinstance(new, list):
			raise TypeError("multipliers must be set to an list")
			
		multipliers = new
		
	def GetMultipliers():
		return(multipliers)
		
	def GetRent(num):
		return multipliers[num]
		
	def SetIsMorgaged(new):
		if not isinstance(new, bool):
			raise TypeError("isMorgaged must be set to a boolean")
			
		isMorgaged = new
		
	def GetIsMorgaged():
		return isMorgaged
		
	def SetGroup():
		if not isinstance(new, str):
			raise TypeError("group must be set to a string")
			
		group = new
		
	def GetGroup():
		return group
		
	def SetOwner(new):
		if not isinstance(new, Player):
			raise TypeError("owner must be set to a Player")
		
		owner = new
			
	def GetOwner():
		return owner