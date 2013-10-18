#
# MAC0425/5730 - Inteligencia Artificial - EP1 @ 2013.2
# Autor: Bruno Nunes Leal Faria - nUSP: 8765551
#
# FILE: environment.py
#
import agent
import search
import time

a = agent.agent()

# enviroment class
# @map - multi dimensional array to hold mine map
# @agent - search type to execute
class environment:
	def __init__(self):
		self.map = [[]]
		self.graph = {}
		self.size = 0
		self.gold_count = 0
		self.gold_left = []
		self.gold_locations = []
		self.search_type = None
	
	# creates matrix from file
	def create_matrix(self, stream):
		x = 0
		y = 0
		# read dimension
		c = stream.read(1)
		# take not of gold mine size
		self.size = c
		if c.isdigit():
			mine_field = [[0]*int(c) for i in range(int(c))]
		# read newline
			c = stream.read(1) 
			# read the mine map
			while True:
				c = stream.read(1)
				if not c or y > 7:
					self.map = mine_field
					return True
				elif c == "\n":
					y += 1
					x = 0
				else:
					# tracks gold in mine	
					if c == "*":
						self.gold_count += 1
					mine_field[y][x] = c
					x += 1
		else:
			print "Not an integer or invalid range"
		return True

	# creates valid action paths from file
	# valid moves are Up, Down, Left, Right and Pickup
	# if 1 = Wall
	# if * = Gold
	def create_graph(self):
		graph = {}
		i = 0
		for x in range(int(self.size)):
		 	for y in range(int(self.size)):
		 		path = []
		 		if self.map[y][x] != "1":
			 		# gold
			 		if self.map[y][x] == "*":
			 			path.append((y*int(self.size))+x)
			 			self.gold_locations.append((y*int(self.size))+x)
			 		# right
			 		if x+1 <= int(self.size) - 1 and self.map[y][x+1] != "1": 
			 			path.append((y*int(self.size))+x+1)
			 		# left
			 		if self.map[y][x-1] != "1" and x-1 >= 0:
			 			path.append((y*int(self.size))+x-1)
			 		# down
			 		if y+1 <= int(self.size) - 1 and self.map[y+1][x] != "1":
			 			path.append(((y+1)*int(self.size))+x)
			 		# up 
			 		if self.map[y-1][x] != "1" and y-1 >= 0:
			 			path.append(((y-1)*int(self.size))+x)
			 		graph[(y*int(self.size))+x] = path

		# saves graph path
		self.graph = graph
		# saves gold location
		for gold in self.gold_locations:
			self.gold_left.append(gold)	
