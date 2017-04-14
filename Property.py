import Player
from Tile import Tile

class Property(Tile):

	def __init__(self, name, type, boardPos, buyValue, rentValues, houseCost, group):
	
		Tile.__init__(self, name, type, boardPos)
		
		if not isinstance(buyValue, int):
			raise TypeError("buyValue must be set to an int")
		self.buyValue = buyValue
		
		if not isinstance(rentValues, list):
			raise TypeError("rentValues must be set to a list")
		self.rentValues = rentValues
		
		if not isinstance(houseCost, int):
			raise TypeError("houseCost must be set to an int")
		self.houseCost = houseCost
		
		if not isinstance(group, str):
			raise TypeError("group must be set to a string")
		self.group = group
		
		self.numHouses = 0
		self.isMorgaged = False
		self.owner = ""
		
	def SetBuyValue(self, new):
		if not isinstance(new, int):
			raise TypeError("buyValue must be set to an int")
			
		self.buyValue = new	
	
	def GetBuyValue(self):
		return self.buyValue
		
	def SetRentValues(self, new):
		if not isinstance(new, list):
			raise TypeError("rentValues must be set to a list")
			
		self.rentValues = new
		
	def GetRentValues(self):
		return self.rentValues
		
	def GetRent(self):
		return self.rentValues[self.numHouses]
		
	def SetNumHouses(self, new):
		if not isinstance(new, int):
			raise TypeError("numHouses must be set to an int")
		
		self.numHouses = new
			
	def GetNumHouses(self):
		return self.numHouses
		
	def SetHouseCost(self, new):
		if not isinstance(new, int):
			raise TypeError("houseCost must be set to an int")
			
		self.houseCost = new
			
	def GetHouseCost(self):
		return self.houseCost
		
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
		