#
# MAC0425/5730 - Inteligencia Artificial - EP1 @ 2013.2
# Autor: Bruno Nunes Leal Faria - nUSP: 8765551
#
# FILE: environment.py
#
import agent
import search

a = agent.agent()

# enviroment class
# @map - multi dimensional array to hold mine map
# @agent - search type to execute
class environment:
	def __init__(self):
		self.map = [[]]
		self.size = 0
		self.gold_count = 0
		self.gold_locations = []
		self.search_type = None
	def execute(self):
		if self.search_type == "L":
			while self.gold_count > 0:
				# initial pos
				ini_y = a.pos_y
				ini_x = a.pos_x
				# resets visited
				a.visited = []
				#start searching for each gold
				
				search.bfs(self, a, ini_y, ini_x)

		elif self.search_type == "P":
			search.dfs(self, a, ini_y, ini_x)
		elif self.search_type == "A":
			search.astar(self, a, ini_y, ini_x)
		return False


