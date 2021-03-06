import random

class Dice():


	
	def __init__(self, dice = [6,6], JailRoll = 3):
		if not isinstance(dice, list):
			raise TypeError("dice must be a list")
			
		if not isinstance(JailRoll, int):
			raise TypeError("JailOnRoll must be set to an integer")
			
		self.dice = dice
		self.JailOnRoll = JailRoll
		
		self.DoublesCount = 0
	
	def GetNumDice(self):
		return len(self.dice)
		
	def SetDice(self, newDice ):
		self.dice = newDice
	
	def SetDoublesCount(self, newCount):
		self.DoublesCount = newCount
	
	def GetDoublesCount(self):
		return self.DoublesCount
		
	def IncrementDoublesCount(self):
		self.DoublesCount += 1
		
	def SetJailOnRoll(self, onRoll ):
		self.JailOnRoll = onRoll
		
	def GetJailonRoll(self):
		return self.JailOnRoll
		
	def RollDice(self):
		rolls = []
		for die in self.dice:
			rolls.append(random.randrange(1, die + 1))
			
		if self.checkDoubles(rolls):
			self.DoublesCount += 1
		else:
			self.DoublesCount = 0
			
		return sum(rolls)
		
	def checkDoubles(self, rolls):
		return all(x == rolls[0] for x in rolls)