#
# MAC0425/5730 - Inteligencia Artificial - EP1 @ 2013.2
# Autor: Bruno Nunes Leal Faria - nUSP: 8765551
#
# FILE: graph.py
#

# structure to hold the graph that will be used to perform the search
class Graph:
	def __init__(self):
		self.G = {}
		
	def add_edge(self, node_i, node_j, weight=0):
		if node_i in self.G.keys():
			self.G[node_i].append((node_j, weight))
		else:
			self.G[node_i] = [(node_j, weight)]
		if node_j in self.G.keys():
			self.G[node_j].append((node_i, weight))
		else:
			self.G[node_j] = [(node_i, weight)]
		
	def neighbors(self, node):
		if node in self.G.keys():
			return [neighbor for (neighbor, weight) in self.G[node]]
		else:
			return None
		
	def get_weight_of_edge(self, node_i, node_j):
		neighbor_nodes = self.G[node_i]
		if node_j in self.neighbors(node_i):
			# Assumes only one weight will be in list
			weight = [weight for (node, weight) in neighbor_nodes if node == node_j].pop()
			return weight
		else:
			return None
		
	def __len__(self):
		return len(self.G)

	def __str__(self):
		return str(self.G)
