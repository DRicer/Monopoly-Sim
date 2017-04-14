

class Board():


	def __init__(self, width = 11, height = 11, evenBuild = True, morgagePercent = 0.5, morgageInterest = 1.1, availableHouses = 32, availableHotel = 12 , houseSellPercent = 1.0):
	
		if not isinstance(width, int):
				raise TypeError("width must be set to an integer")
		self.width = width
		
		if not isinstance(height, int):
				raise TypeError("height must be set to an integer")
		self.height = height
		
		if not isinstance(evenBuild, bool):
				raise TypeError("evenBuild must be set to a boolean")
		self.evenBuild = evenBuild
		
		if not isinstance(morgagePercent, float):
				raise TypeError("morgagePercent must be set to a float")
		self.morgagePercent = morgagePercent
		
		if not isinstance(morgageInterest, float):
				raise TypeError("morgageInterest must be set to a float")
		self.morgageInterest = morgageInterest
		
		if not isinstance(availableHouses, int):
				raise TypeError("availableHouses must be set to an integer")
		self.availableHouses = availableHouses
		
		if not isinstance(availableHotel, int):
				raise TypeError("availableHotel must be set to an integer")
		self.availableHotel = availableHotel
		
		if not isinstance(houseSellPercent, float):
				raise TypeError("houseSellPercent must be set to a float")
		self.houseSellPercent = houseSellPercent

	def SetEvenBuild(self, even):
		self.evenBuild = even
		
	def GetEvenBuild(self):
		return self.evenBuild
		
		
	def SetDimensions(self, newHeight, newWidth):
	
		if not isinstance(newWidth, int):
			raise TypeError("width must be set to an integer")
	
		if not isinstance(newHeight, int):
			raise TypeError("height must be set to an integer")
		
		self.height = newHeight
		self.width = newWidth
		
	def GetDimentions(self):
		return [self.height, self.width]
		
	def SetMorgagePercent(self, new):
	
		if not isinstance(new, float):
			raise TypeError("morgagePercent must be set to a float")
		
		self.morgagePercent = new
		
	def GetMorgagePercent(self):
		return self.morgagePercent
		
	def SetMorgageInterest(self, new):
	
		if not isinstance(new, float):
			raise TypeError("morgageInterest must be set to a float")
			
		self.morgageInterest = new
		
	def GetMorgageInterest(self):
		return self.morgageInterest
		
	def SetAvailableHouses(self, new):
	
		if not isinstance(new, int):
			raise TypeError("availableHouses must be set to an integer")
			
		self.availableHouses = new
		
	def GetAvailableHouses(self):
		return self.availableHouses
		
	def IncAvailableHouses(self):
		self.availableHouses += 1
		
	def DecAvailableHouses(self):
		self.availableHouses -= 1
 		
	def SetAvailableHotels(self, new):
	
		if not isinstance(new, int):
			raise TypeError("availableHotel must be set to an integer")
			
		self.availableHotel = new
		
	def GetAvailableHotels(self):
		return self.availableHotel
		
		
	def IncAvailableHotels(self):
		self.availableHouses += 1
		
	def DecAvailableHotels(self):
		self.availableHouses -= 1
		
	def SetHouseSellPercent(self, new):
		if not isinstance(new, float):
			raise TypeError("houseSellPercent must be set to a float")
			
		self.houseSellPercent = new
		
	def GetHouseSellPercent(self):
		return self.houseSellPercent
