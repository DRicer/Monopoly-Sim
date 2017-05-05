from tkinter import *

class MonopolyGUI():

	def __init__(self):
		self.root = Tk()
		self.tiles = {}
		self.owner = {}
		self.playerSpaces = {}
		self.houses = {}
		self.playerCashBox = ["","","",""]
		self.playerCash = ["","","",""]
	def load(self, dimentions, properties, startCash):
		
		count = 0
		background = Canvas(height = (75 * dimentions[0]), width = (75 * dimentions[1]), bg = "black")
		background.pack()
		for i in range(0,dimentions[0]):
			for j in range(0,dimentions[1]):
				#check if square is just filler
				if j > 0 and j < dimentions[1] - 1 and i > 0 and i < dimentions[0] - 1:
					if j == 1 and i == 1:
						self.playerCashBox[0] = Canvas(background, height = 73, width = 73, bg = "red")
						self.playerCashBox[0].grid_propagate(False)
						self.playerCashBox[0].grid(column = j, row = i, padx = 1, pady = 1)
						player = Label(self.playerCashBox[0], text = "Player 0's Cash:", anchor = "n", wraplength = 75, font=("Courier", 8))
						player.grid_propagate(False)
						player.grid()
						
						self.playerCash[0] = Label(self.playerCashBox[0], text = "£" + str(startCash), anchor = "n", wraplength = 75, font=("Courier", 8))
						self.playerCash[0].grid_propagate(False)
						self.playerCash[0].grid()
						
					elif j == 1 and i == 2:
						self.playerCashBox[2] = Canvas(background, height = 73, width = 73, bg = "blue")
						self.playerCashBox[2].grid_propagate(False)
						self.playerCashBox[2].grid(column = j, row = i, padx = 1, pady = 1)
						player = Label(self.playerCashBox[2], text = "Player 2's Cash:", anchor = "n", wraplength = 75, font=("Courier", 8))
						player.grid_propagate(False)
						player.grid()
						
						self.playerCash[2] = Label(self.playerCashBox[2], text = "£" + str(startCash), anchor = "n", wraplength = 75, font=("Courier", 8))
						self.playerCash[2].grid_propagate(False)
						self.playerCash[2].grid()
						
					elif j == 2 and i == 1:
						self.playerCashBox[1] = Canvas(background, height = 73, width = 73, bg = "green")
						self.playerCashBox[1].grid_propagate(False)
						self.playerCashBox[1].grid(column = j, row = i, padx = 1, pady = 1)
						player = Label(self.playerCashBox[1], text = "Player 1's Cash:", anchor = "n", wraplength = 75, font=("Courier", 8))
						player.grid_propagate(False)
						player.grid()
						
						self.playerCash[1] = Label(self.playerCashBox[1], text = "£" + str(startCash), anchor = "n", wraplength = 75, font=("Courier", 8))
						self.playerCash[1].grid_propagate(False)
						self.playerCash[1].grid()
						
					elif j== 2 and i == 2:
						self.playerCashBox[3] = Canvas(background, height = 73, width = 73, bg = "yellow")
						self.playerCashBox[3].grid_propagate(False)
						self.playerCashBox[3].grid(column = j, row = i, padx = 1, pady = 1)
						player = Label(self.playerCashBox[3], text = "Player 3's Cash:", anchor = "n", wraplength = 75, font=("Courier", 8))
						player.grid_propagate(False)
						player.grid()
						
						self.playerCash[3] = Label(self.playerCashBox[3], text = "£" + str(startCash), anchor = "n", wraplength = 75, font=("Courier", 8))
						self.playerCash[3].grid_propagate(False)
						self.playerCash[3].grid()
						
					else:
						filler = Canvas(background, height = 75, width = 75, bd = 0, bg = "black", highlightthickness=0)
						filler.grid(column = i, row = j, padx = 1, pady = 1)
					
				else:
					#create a used tile
					
					if count < dimentions[0]:
						#top row
						self.tiles[count] = Canvas(background, height = 73, width = 73)
						self.playerSpaces[count] = []
						self.playerSpaces[count].append(self.tiles[count].create_oval(60, 60, 70, 70))
						self.playerSpaces[count].append(self.tiles[count].create_oval(45, 60, 55, 70))
						self.playerSpaces[count].append(self.tiles[count].create_oval(30, 60, 40, 70))
						self.playerSpaces[count].append(self.tiles[count].create_oval(15, 60, 25, 70))
						
						name = Label(self.tiles[count], text = properties[count].GetName(), anchor = "n", wraplength = 75, font=("Courier", 6))
						name.grid_propagate(False)
						name.grid()
						
						if hasattr(properties[count], 'GetBuyValue'):
							self.owner[count] = self.tiles[count].create_oval(70, 35, 74, 45)
							self.houses[count] = []
							self.houses[count].append(self.tiles[count].create_rectangle(15, 50, 25, 55))
							self.houses[count].append(self.tiles[count].create_rectangle(25, 50, 35, 55))
							self.houses[count].append(self.tiles[count].create_rectangle(35, 50, 45, 55))
							self.houses[count].append(self.tiles[count].create_rectangle(45, 50, 55, 55))
							cost = Label(self.tiles[count], text = "£" + str(properties[count].GetBuyValue()), anchor = "s", wraplength = 75, font=("Courier", 6))
							cost.grid_propagate(False)
							cost.grid()
						self.tiles[count].grid_propagate(False)
						self.tiles[count].grid(column = j, row = i, padx = 1, pady = 1)
						
					elif (count) % dimentions[0] == 0:
						#left column
						property = len(properties) - (count / dimentions[0])
						self.tiles[property] = Canvas(background, height = 73, width = 73)
						self.playerSpaces[property] = []
						self.playerSpaces[property].append(self.tiles[property].create_oval(60, 60, 70, 70))
						self.playerSpaces[property].append(self.tiles[property].create_oval(45, 60, 55, 70))
						self.playerSpaces[property].append(self.tiles[property].create_oval(30, 60, 40, 70))
						self.playerSpaces[property].append(self.tiles[property].create_oval(15, 60, 25, 70))
						
						name = Label(self.tiles[property], text = properties[property].GetName(), anchor = "n", wraplength = 75, font=("Courier", 6))
						name.grid_propagate(False)
						name.grid()
						
						if hasattr(properties[property], 'GetBuyValue'):
							self.owner[property] = self.tiles[property].create_oval(70, 35, 74, 45)
							self.houses[property] = []
							self.houses[property].append(self.tiles[property].create_rectangle(15, 50, 25, 55))
							self.houses[property].append(self.tiles[property].create_rectangle(25, 50, 35, 55))
							self.houses[property].append(self.tiles[property].create_rectangle(35, 50, 45, 55))
							self.houses[property].append(self.tiles[property].create_rectangle(45, 50, 55, 55))
							cost = Label(self.tiles[property], text = "£" + str(properties[property].GetBuyValue()), anchor = "s", wraplength = 75, font=("Courier", 6))
							cost.grid_propagate(False)
							cost.grid()
						self.tiles[property].grid_propagate(False)
						self.tiles[property].grid(column = j, row = i, padx = 1, pady = 1)
						
					elif (count + 1) % dimentions[0] == 0:
						#right column
						property = (count // dimentions[0]) + (dimentions[0] - 1)
						
						self.tiles[property] = Canvas(background, height = 73, width = 73)
						self.playerSpaces[property] = []
						self.playerSpaces[property].append(self.tiles[property].create_oval(60, 60, 70, 70))
						self.playerSpaces[property].append(self.tiles[property].create_oval(45, 60, 55, 70))
						self.playerSpaces[property].append(self.tiles[property].create_oval(30, 60, 40, 70))
						self.playerSpaces[property].append(self.tiles[property].create_oval(15, 60, 25, 70))
						
						
						name = Label(self.tiles[property], text = properties[property].GetName(), anchor = "n", wraplength = 75, font=("Courier", 6))
						name.grid_propagate(False)
						name.grid()
						
						if hasattr(properties[property], 'GetBuyValue'):
							self.owner[property] = self.tiles[property].create_oval(70, 35, 74, 45)
							self.houses[property] = []
							self.houses[property].append(self.tiles[property].create_rectangle(15, 50, 25, 55))
							self.houses[property].append(self.tiles[property].create_rectangle(25, 50, 35, 55))
							self.houses[property].append(self.tiles[property].create_rectangle(35, 50, 45, 55))
							self.houses[property].append(self.tiles[property].create_rectangle(45, 50, 55, 55))
							cost = Label(self.tiles[property], text = "£" + str(properties[property].GetBuyValue()), anchor = "s", wraplength = 75, font=("Courier", 6))
							cost.grid_propagate(False)
							cost.grid()
						self.tiles[property].grid_propagate(False)
						self.tiles[property].grid(column = j, row = i, padx = 1, pady = 1)
						
					elif i == dimentions[0] - 1:
						#bottom row
						invj = list(range(-(dimentions[1] - 3),dimentions[1] - 2, 2))
						invj = list(reversed(invj))
						property = ((len(properties) - (dimentions[0] * dimentions[1] - count)) - (dimentions[0] - 2)) + invj[j-1]
						self.tiles[property] = Canvas(background, height = 73, width = 73)
						self.playerSpaces[property] = []
						self.playerSpaces[property].append(self.tiles[property].create_oval(60, 60, 70, 70))
						self.playerSpaces[property].append(self.tiles[property].create_oval(45, 60, 55, 70))
						self.playerSpaces[property].append(self.tiles[property].create_oval(30, 60, 40, 70))
						self.playerSpaces[property].append(self.tiles[property].create_oval(15, 60, 25, 70))
						
						
						
						name = Label(self.tiles[property], text = properties[property].GetName(), anchor = "n", wraplength = 75, font=("Courier", 6 ))
						name.grid_propagate(False)
						name.grid()
						
						if hasattr(properties[property], 'GetBuyValue'):
							self.owner[property] = self.tiles[property].create_oval(70, 35, 74, 45)
							self.houses[property] = []
							self.houses[property].append(self.tiles[property].create_rectangle(15, 50, 25, 55))
							self.houses[property].append(self.tiles[property].create_rectangle(25, 50, 35, 55))
							self.houses[property].append(self.tiles[property].create_rectangle(35, 50, 45, 55))
							self.houses[property].append(self.tiles[property].create_rectangle(45, 50, 55, 55))
							cost = Label(self.tiles[property], text = "£" + str(properties[property].GetBuyValue()), anchor = "s", wraplength = 75, font=("Courier", 6))
							cost.grid_propagate(False)
							cost.grid()
						self.tiles[property].grid_propagate(False)
						self.tiles[property].grid(column = j, row = i, padx = 1, pady = 1)
						
				count += 1
		return self.root.update()
		
	def update(self, players, oldTile):
	
		def UpdateProperty(player, color):
			ownedPropertys = player.GetOwnedPropertys()
			if ownedPropertys:
				for property in ownedPropertys:
					self.tiles[property.GetBoardPos()].itemconfig(self.owner[property.GetBoardPos()], fill = color)	
					if property.GetType() == "standard":
						for i in range(0,4):
								self.tiles[property.GetBoardPos()].itemconfig(self.houses[property.GetBoardPos()][i], fill = "")
						if property.GetNumHouses() > 4:
							for i in range(0,4):
								self.tiles[property.GetBoardPos()].itemconfig(self.houses[property.GetBoardPos()][i], fill = "red")
						else:
							for i in range(0, property.GetNumHouses()):
								self.tiles[property.GetBoardPos()].itemconfig(self.houses[property.GetBoardPos()][i], fill = "blue")
					
		for player in players:
			self.tiles[oldTile].itemconfig(self.playerSpaces[oldTile][players.index(player)], fill = "")
			if players.index(player) == 0:
				color = "red"
				self.tiles[player.GetBoardPos()].itemconfig(self.playerSpaces[player.GetBoardPos()][players.index(player)], fill = color)
				UpdateProperty(player, color)
				self.playerCash[0].config(text = "£" + str(player.GetCash()))
			elif players.index(player) == 1:
				color = "green"
				self.tiles[player.GetBoardPos()].itemconfig(self.playerSpaces[player.GetBoardPos()][players.index(player)], fill = color)
				UpdateProperty(player, color)
				self.playerCash[1].config(text = "£" + str(player.GetCash()))
			elif players.index(player) == 2:
				color = "blue"
				self.tiles[player.GetBoardPos()].itemconfig(self.playerSpaces[player.GetBoardPos()][players.index(player)], fill = color)
				UpdateProperty(player, color)
				self.playerCash[2].config(text = "£" + str(player.GetCash()))
			elif players.index(player) == 3:
				color = "yellow"
				self.tiles[player.GetBoardPos()].itemconfig(self.playerSpaces[player.GetBoardPos()][players.index(player)], fill = color)
				UpdateProperty(player, color)
				self.playerCash[3].config(text = "£" + str(player.GetCash()))
				
				
		self.root.update()