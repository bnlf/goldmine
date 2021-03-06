#
# MAC0425/5730 - Inteligencia Artificial - EP1 @ 2013.2
# Autor: Bruno Nunes Leal Faria - nUSP: 8765551
#
# FILE: search.py
#
import math
import time
from collections import deque

def bfs(graph, start, end, agent):
	todo = [[start, [start]]]
	while 0 < len(todo):
		(node, path) = todo.pop(0)
		for next_node in graph[node]:
			if next_node in path:
				continue
			elif next_node == end:
				agent.current_state = next_node
				return path + [next_node]
			else:
				todo.append([next_node, path + [next_node]])

def idfs(graph, start, end, depth, path=[], i=0):
	path = path + [start]
	if start == end or i > depth:
		return path
	if not graph.has_key(start):
		return None
	shortest = None
	for node in graph[start]:
		if node not in path:
			i+=1
			newpath = idfs(graph, node, end, depth, path, i)
			if newpath:
				if not shortest or len(newpath) < len(shortest):
					shortest = newpath
	return shortest

# A star search
def astar(env, y, x):
	return True

# estimate cost to get to gold using an heuristic
# f(n) = g(n) + h(n) where h(n) = dist(current_pos,gold_pos)
def estimate_cost(state, gold_pos, size):
	# cost to move inside the mine
	cost_step = -1
	# reward for picking up a gold
	cost_gold = 4 * int(size)
	
	# heuristic - number of steps from current position to gold position
	num_steps = math.fabs(gold_pos[0]-state[0]) + math.fabs(gold_pos[1]-state[1])
	cost = (cost_step*num_steps)+cost_gold
	return cost
