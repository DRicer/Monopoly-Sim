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
			
				if j > 0 and j < dimentions[1] - 1 and i > 0 and i < dimentions[0] - 1:
				
					tiles[count] = Canvas(background, height = 75, width = 75, bd = 0, bg = "black", highlightthickness=0)
					tiles[count].grid(column = i, row = j, padx = 1, pady = 1)
					
				else:
				
					tiles[count] = Canvas(background, height = 73, width = 73)
					tiles[count].grid_propagate(False)
					tiles[count].grid(column = j, row = i, padx = 1, pady = 1)
					
					if count < dimentions[0]:
					
						name = Label(tiles[count], text = properties[count].GetName(), anchor = "n", wraplength = 75)
						name.grid_propagate(False)
						name.grid()
						
						if hasattr(properties[count], 'GetBuyValue'):
							cost = Label(tiles[count], text = "£" + str(properties[count].GetBuyValue()), anchor = "s", wraplength = 75)
							cost.grid_propagate(False)
							cost.grid()
							
					elif (count) % dimentions[0] == 0:
					
						property = len(properties) - (count / dimentions[0])
						name = Label(tiles[count], text = properties[property].GetName(), anchor = "n", wraplength = 75)
						name.grid_propagate(False)
						name.grid()
						
						if hasattr(properties[property], 'GetBuyValue'):
							cost = Label(tiles[count], text = "£" + str(properties[property].GetBuyValue()), anchor = "s", wraplength = 75)
							cost.grid_propagate(False)
							cost.grid()
							
					elif (count + 1) % dimentions[0] == 0:
					
						property = (count // dimentions[0]) + (dimentions[0] - 1)
						name = Label(tiles[count], text = properties[property].GetName(), anchor = "n", wraplength = 75)
						name.grid_propagate(False)
						name.grid()
						
						if hasattr(properties[property], 'GetBuyValue'):
							cost = Label(tiles[count], text = "£" + str(properties[property].GetBuyValue()), anchor = "s", wraplength = 75)
							cost.grid_propagate(False)
							cost.grid()
					
					elif j == dimentions[0] - 1:
						
						property = len(properties) - (count / dimentions[0])
						name = Label(tiles[count], text = properties[property].GetName(), anchor = "n", wraplength = 75)
						name.grid_propagate(False)
						name.grid()
						
						if hasattr(properties[property], 'GetBuyValue'):
							cost = Label(tiles[count], text = "£" + str(properties[property].GetBuyValue()), anchor = "s", wraplength = 75)
							cost.grid_propagate(False)
							cost.grid()
							
				count += 1
		return root.mainloop()