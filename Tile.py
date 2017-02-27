

class Tile():

	def __init__(self, type, boardPos, event):
		if not isinstance(type, str):
			raise TypeError("type must be set to a string")
		self.type = type
			
		if not isinstance(boardPos, int):
			raise TypeError("boardPos must be set to a integer")
		self.boardPos = boardPos
		
		if not isinstance(event, str):
			raise TypeError("event must be set to a string")
		self.event = event
	
	def SetTileType(new):
	
		if not isinstance(new, str):
			raise TypeError("type must be set to a string")
		
		type = new
	
	def GetType():
		return type
		
	def SetBoardPos(new):
	
		if not isinstance(new, int):
			raise TypeError("boardPos must be set to a integer")
			
		boardPos = new
		
	def GetBoardPos():
		return boardPos
		
	def SetEvent(new):
		if not isinstance(new, str):
			raise TypeError("event must be set to a string")
		
		event = new
		
	def GetEvent():
		return event
		
	def DoEvent():
		