

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

	def SetEvenBuild(even):
		evenBuild = even
		
	def GetEvenBuild():
		return evenBuild
		
		
	def SetDimensions(newHeight, newWidth):
	
		if not isinstance(newWidth, int):
			raise TypeError("width must be set to an integer")
	
		if not isinstance(newHeight, int):
			raise TypeError("height must be set to an integer")
		
		height = newHeight
		width = newWidth
		
	def GetDimentions():
		return [height, width]
		
	def SetMorgagePercent(new):
	
		if not isinstance(new, float):
			raise TypeError("morgagePercent must be set to a float")
		
		morgagePercent = new
		
	def GetMorgage Percent():
		return morgagePercent
		
	def SetMorgageInterest(new):
	
		if not isinstance(new, float):
			raise TypeError("morgageInterest must be set to a float")
			
		morgageInterest = new
		
	def GetMorgageInterest():
		return morgageInterest
		
	def SetAvailableHouses(new):
	
		if not isinstance(new, int):
			raise TypeError("availableHouses must be set to an integer")
			
		availableHouses = new
		
	def GetAvailableHouses():
		return availableHouses
		
	def IncAvailableHouses():
		availableHouses += 1
		
	def DecAvailableHouses():
		availableHouses -= 1
 		
	def SetAvailableHotels(new):
	
		if not isinstance(new, int):
			raise TypeError("availableHotel must be set to an integer")
			
		availableHotel = new
		
	def GetAvailableHotels():
		return availableHotel
		
		
	def IncAvailableHotels():
		availableHouses += 1
		
	def DecAvailableHotels():
		availableHouses -= 1
		
	def SetHouseSellPercent(new):
		if not isinstance(new, float):
			raise TypeError("houseSellPercent must be set to a float")
			
		houseSellPercent = new
		
	def GetHouseSellPercent():
		return houseSellPercent
