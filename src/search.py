#
# MAC0425/5730 - Inteligencia Artificial - EP1 @ 2013.2
# Autor: Bruno Nunes Leal Faria - nUSP: 8765551
#
# FILE: search.py
#
# import time
import math

# Breadth First Search
def bfs(env, agent, y, x):
	queue = []
	q_buffer = []
	# initial append root
	queue.append([y,x])
	
	while queue:
		# saves current state
		current_state = queue[0]
		# get from queue list
		queue.pop(0)

		# debug
		# for x in range(8):
		# 	for y in range(8): 
		# 		if current_state[0] == x and current_state[1] == y:
		# 			print "x",
		# 		else:
		# 			print env.map[x][y],
		# 	print "\n",
		# print
		# time.sleep(0.5)

		# is it gold?
		if env.map[current_state[0]][current_state[1]] == "*":
			# updates information
			env.map[current_state[0]][current_state[1]] = "0"
			env.gold_count-=1
			# updates agent pos for next batch
			agent.pos_y = current_state[0]
			agent.pos_x = current_state[1]
			# saves action
			q_buffer.append("P")
			agent.visited.append(current_state)
			# we are done here
			queue = []
			break
		else:
			# take notes of visited places
			agent.visited.append(current_state)

			# move right
			if agent.can_move_right(env.map, current_state):
				queue.append([current_state[0], current_state[1]+1])
				q_buffer.append("D")
			# move left
			if agent.can_move_left(env.map, current_state):
				queue.append([current_state[0], current_state[1]-1])
				q_buffer.append("E")
			# move up
			if agent.can_move_up(env.map, current_state):
				queue.append([current_state[0]-1, current_state[1]])
				q_buffer.append("C")
			# move down
			if agent.can_move_down(env.map, current_state):
				queue.append([current_state[0]+1, current_state[1]])
				q_buffer.append("B")

	for c in q_buffer:
		print c,
	return True

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