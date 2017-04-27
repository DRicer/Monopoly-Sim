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
	
	def SetDoubleCount(self, newCount):
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
			rolls.append(random.randrange(1, die))
			
		if self.checkDoubles(self, rolls):
			self.DoublesCount += 1
		else:
			self.DoublesCount = 0
			
		return rolls.sum()
		
	def checkDoubles(self, iterator):
		iterator = iter(iterator)
		try:
			first = next(iterator)
		except StopIteration:
			return True
		return all(first == rest for rest in iterator)