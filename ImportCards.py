from Card import Card

class ImportCards():
	
	def loadCards(self):
		cardList = {}
		chance = []
		chest = []
		decodedAtions = {}
		cards = open("Cards.txt")
		for line in cards:
			params = line.split(";")
			type = int(params[0])
			text = params[1]
			params[2] = params[2].strip("[")
			params[2] = params[2].strip("]")
			actions = params[2].split(":")
			for i in range(0,len(actions)):
				action = actions[i].split("(")[0]
				arguments = actions[i].split("(")[1]
				decodedAtions[action] = arguments.strip(")")
				if type = 1:
					chance.append(Card(type, text, decodedAtions))
				elif type = 2:
					chest.append(Card(type, text, decodedAtions))
					
				cardList["chance"] = chance
				cardList["chest"] = chest
		cards.close()
		return cardList