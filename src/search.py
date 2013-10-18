#
# MAC0425/5730 - Inteligencia Artificial - EP1 @ 2013.2
# Autor: Bruno Nunes Leal Faria - nUSP: 8765551
#
# FILE: search.py
#
import math
import time
import node
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

# Deapth First Search
def dfs(env, y, x):
	return True

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
