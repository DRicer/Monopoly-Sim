import Player from Player
import Tile from Tile

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
		
	def SetBuyValue(new):
		if not isinstance(new, int):
			raise TypeError("buyValue must be set to an int")
			
		buyValue = new	
	
	def GetbuyValue():
		return buyValue
		
	def SetRentValues(new):
		if not isinstance(new, list):
			raise TypeError("rentValues must be set to a list")
			
		rentValues = new
		
	def GetRentValues():
		return rentValues
		
	def GetRent():
		return rentValues[numHouses]
		
	def SetNumHouses(new):
		if not isinstance(new, int):
			raise TypeError("numHouses must be set to an int")
		
		numHouses = new
			
	def GetNumHouses():
		return numHouses
		
	def SetHouseCost(new):
		if not isinstance(new, int):
			raise TypeError("houseCost must be set to an int")
			
		houseCost = new
			
	def GetHouseCost():
		return houseCost
		
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
		