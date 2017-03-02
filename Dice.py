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
	
	def GetNumDice():
		return len(dice)
		
	def SetDice( newDice ):
		dice = newDice
	
	def SetDoubleCount(newCount):
		DoublesCount = newCount
	
	def GetdoublesCount():
		return DoublesCount
		
	def IncrementDoublesCount():
		DoublesCount += 1
		
	def SetJailOnRoll( onRoll ):
		JailOnRoll = onRoll
		
	def GetJailonRoll():
		return JailOnRoll
		
	def RollDice():
		rolls = []
		for die in dice:
			rolls.append(random.randrange(1, die))
			
		if checkDoubles(rolls):
			DoublesCount += 1
		else:
			DoublesCount = 0
			
		return rolls.sum()
		
	def checkDoubles(iterator):
		iterator = iter(iterator)
		try:
			first = next(iterator)
		except StopIteration:
			return True
		return all(first == rest for rest in iterator)