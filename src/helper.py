#
# MAC0425/5730 - Inteligencia Artificial - EP1 @ 2013.2
# Autor: Bruno Nunes Leal Faria - nUSP: 8765551
#
# FILE: helper.py
#

import sys
import filecmp
import graph

def get_graph(matrix_file_path):
	# Given an adjacency matrix file path, return a graph of the network
	input_file = open(matrix_file_path, 'r')
	#G = nx.Graph()
	G = graph.Graph()
	node_i = 0
	for line in input_file:
		# First, remove whitespace
		line = line.replace(' ', '').strip()
		if len(line) is 0:
			break
			
		# Then, remove comments
		if line[0] == '#':
			pass # comment line
			
		# Finally, add edges to graph G
		else:
			for node_j, weight in enumerate(line):
				weight = int(weight)
				if weight > 0:
					G.add_edge(node_i, node_j, weight)
			node_i += 1
	return G
		 
def get_heuristic_array(heuristic_file_path):
	input_file = open(heuristic_file_path, 'r')
	heuristic_array = []
	row = 0
	for line in input_file:
		line = line.replace(' ', '').strip()
		if len(line) is 0:
			break
		
		if line[0] == '#':
			pass
			
		else:
			heuristic_array.append([])
			for weight in line:
				weight = int(weight)
				heuristic_array[row].append(weight)
			row += 1
	return heuristic_array
			 
def remove_whitespace_and_comments(line):
	line = line.replace(' ', '').strip()
	if len(line) is 0 or line[0] == '#':
		return ''
	else:
		return line
