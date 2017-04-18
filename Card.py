

class Card():

	#chance: type = 1, community chest: type = 2 
	def __init__(self, type, text, actions):
	
		if not isinstance(type, int):
				raise TypeError("type must be set to an integer")
		self.type = type
		
		if not isinstance(text, str):
				raise TypeError("card text must be a string")
		self.text = text
		
		if not isinstance(actions, dict):
				raise TypeError("actions must be a dict")
		self.actions = actions
	
	def GetType():
		return self.type
		
	def GetText():
		return self.text
	
	def GetActions():
		