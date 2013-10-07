#
# MAC0425/5730 - Inteligencia Artificial - EP1 @ 2013.2
# Autor: Bruno Nunes Leal Faria - nUSP: 8765551
#
# FILE: agent.py
#
import math

# agent class
# @
# @
class agent:
	def __init__(self):
		self.action = None
		self.pos_y = 0
		self.pos_x = 0
		self.visited = []
		self.gold_count = 0
	def current_state(self):
		state = []
		state.append([self.pos_y, self.pos_x])
		return state
	def can_move_right(self, envmap, state):
		if valid_action(self.visited, envmap, state[0], state[1]+1):
			return True
		return False
	def can_move_left(self, envmap, state):
		if valid_action(self.visited, envmap, state[0], state[1]-1):
			return True
		return False
	def can_move_up(self, envmap, state):
		if valid_action(self.visited, envmap, state[0]-1, state[1]):
			return True
		return False
	def can_move_down(self, envmap, state):
		if valid_action(self.visited, envmap, state[0]+1, state[1]):
			return True
		return False

def valid_action(visited, envmap, pos_y, pos_x):
	if pos_y in range(0,len(envmap)) and pos_x in range(0, len(envmap)) and [pos_y, pos_x] not in visited:
		if envmap[pos_y][pos_x] == "0":
			return True
		elif envmap[pos_y][pos_x] == "*":
			return True
	return False

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
