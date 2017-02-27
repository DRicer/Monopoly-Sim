import random

class Dice():

	DoublesCount = 0

	
	def __init__(self, dice, JailRoll):
		if not isinstance(dice, list):
			raise TypeError("dice must be a list")
			
		if not isinstance(JailRoll, int):
			raise TypeError("JailOnRoll must be set to an integer")
			
		self.Dice = dice
		self.JailOnRoll = JailRoll
	
	def GetNumDice():
		return len(Dice)
		
	def SetDice( newDice ):
		Dice = newDice
	
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
		roll = 0
		for die in Dice:
			roll += random.randrange(1, die)
			
		return roll