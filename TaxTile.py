from Tile import Tile

class TaxTile(Tile):

	def __init__(self, name, type, boardPos, tax):
	
		Tile.__init__(self, name, type, boardPos)
		
		if not isinstance(tax, int):
			raise TypeError("tax must be set to an int")
		self.tax = tax
		
	def setTax(self, new):
		if not isinstance(tax, int):
			raise TypeError("tax must be set to an int")
		self.tax = tax
		
		
	def GetTax(self):
		return self.tax