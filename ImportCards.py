from Card import Card

class ImportCards():
	
	def loadCards():
		cardlist = []
		cards = open("Cards.txt")
			for line in cards:
				params = line.split(";")
				type = int(params[1])
				text = params[2]
				params[3] = params[3].strip("[", "]")
				actions = params[3].split(":")
				for i in range(0,len(actions)):
					action = actions.split("(")[0]
					arguments = actions.split("(")[1]
					decodecAtions[action] = arguments.strip(")")
				cardList.append(Card(type, text, decodedAtions))	
			properties.close()
		return cardList