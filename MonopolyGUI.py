from tkinter import *

class MonopolyGUI():
	
	
	def load(self, dimentions, properties):
		root = Tk()
		tiles = {}
		count = 0
		background = Canvas(height = (75 * dimentions[0]), width = (75 * dimentions[1]), bg = "black")
		background.pack()
		for i in range(0,dimentions[0]):
			for j in range(0,dimentions[1]):
				#check if square is just filler
				if j > 0 and j < dimentions[1] - 1 and i > 0 and i < dimentions[0] - 1:
					
					filler = Canvas(background, height = 75, width = 75, bd = 0, bg = "black", highlightthickness=0)
					filler.grid(column = i, row = j, padx = 1, pady = 1)
					
				else:
					#create a used tile
					
					if count < dimentions[0]:
						#top row
						tiles[count] = Canvas(background, height = 73, width = 73)
						tiles[count].grid_propagate(False)
						tiles[count].grid(column = j, row = i, padx = 1, pady = 1)
						
						name = Label(tiles[count], text = properties[count].GetName(), anchor = "n", wraplength = 75)
						name.grid_propagate(False)
						name.grid()
						
						if hasattr(properties[count], 'GetBuyValue'):
							cost = Label(tiles[count], text = "£" + str(properties[count].GetBuyValue()), anchor = "s", wraplength = 75)
							cost.grid_propagate(False)
							cost.grid()
							
					elif (count) % dimentions[0] == 0:
						#left column
						property = len(properties) - (count / dimentions[0])
						tiles[property] = Canvas(background, height = 73, width = 73)
						tiles[property].grid_propagate(False)
						tiles[property].grid(column = j, row = i, padx = 1, pady = 1)
						name = Label(tiles[property], text = properties[property].GetName(), anchor = "n", wraplength = 75)
						name.grid_propagate(False)
						name.grid()
						
						if hasattr(properties[property], 'GetBuyValue'):
							cost = Label(tiles[property], text = "£" + str(properties[property].GetBuyValue()), anchor = "s", wraplength = 75)
							cost.grid_propagate(False)
							cost.grid()
							
					elif (count + 1) % dimentions[0] == 0:
						#right column
						property = (count // dimentions[0]) + (dimentions[0] - 1)
						
						tiles[property] = Canvas(background, height = 73, width = 73)
						tiles[property].grid_propagate(False)
						tiles[property].grid(column = j, row = i, padx = 1, pady = 1)
						
						name = Label(tiles[property], text = properties[property].GetName(), anchor = "n", wraplength = 75)
						name.grid_propagate(False)
						name.grid()
						
						if hasattr(properties[property], 'GetBuyValue'):
							cost = Label(tiles[property], text = "£" + str(properties[property].GetBuyValue()), anchor = "s", wraplength = 75)
							cost.grid_propagate(False)
							cost.grid()
					
					elif i == dimentions[0] - 1:
						#bottom row
						print(count)
						invj = list(range(-(dimentions[1] - 3),dimentions[1] - 2, 2))
						invj = list(reversed(invj))
						print(invj)
						property = ((len(properties) - (dimentions[0] * dimentions[1] - count)) - (dimentions[0] - 2)) + invj[j-1]
						print(property)
						tiles[property] = Canvas(background, height = 73, width = 73)
						tiles[property].grid_propagate(False)
						tiles[property].grid(column = j, row = i, padx = 1, pady = 1)
						
						name = Label(tiles[property], text = properties[property].GetName(), anchor = "n", wraplength = 75)
						name.grid_propagate(False)
						name.grid()
						
						if hasattr(properties[property], 'GetBuyValue'):
							cost = Label(tiles[property], text = "£" + str(properties[property].GetBuyValue()), anchor = "s", wraplength = 75)
							cost.grid_propagate(False)
							cost.grid()
							
				count += 1
		return root.update()
		
	def update(self, players):
		pass