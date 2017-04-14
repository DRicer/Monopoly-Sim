

class Tile():

	def __init__(self, name, type, boardPos):
	
		if not isinstance(name, str):
			raise TypeError("name must be set to a string")
		self.name = name
		
		if not isinstance(type, str):
			raise TypeError("type must be set to a string")
		self.type = type
			
		if not isinstance(boardPos, int):
			raise TypeError("boardPos must be set to a integer")
		self.boardPos = boardPos
		
		
	def SetName(self, new):
		if not isinstance(new, str):
			raise TypeError("name must be set to a string")
			
		self.name = new
		
	def GetName(self):
		return self.name
	
	def SetTileType(self, new):
	
		if not isinstance(new, str):
			raise TypeError("type must be set to a string")
		
		self.type = new
	
	def GetType(self):
		return self.type
		
	def SetBoardPos(self, new):
	
		if not isinstance(new, int):
			raise TypeError("boardPos must be set to a integer")
			
		self.boardPos = new
		
	def GetBoardPos(self):
		return self.boardPos
		