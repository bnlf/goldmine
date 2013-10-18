#
# MAC0425/5730 - Inteligencia Artificial - EP1 @ 2013.2
# Autor: Bruno Nunes Leal Faria - nUSP: 8765551
#
# FILE: main.py
#

import sys
import environment
import search
import agent
import graph
import helper

# global vars
a = agent.agent()
env = environment.environment()

# checks input arguments
def check_args():
	search_types = ["L", "P", "A"]
	if len(sys.argv) < 3:
		print "Usage: <input_file> <type>"
		print "Search Type: L (largura), P (profundidade) or A (A*)"
		return False
	elif str(sys.argv[2]).upper() not in search_types:
		print "Search type \"%s\" not supported" % (sys.argv[2])
		return False
	else:
		env.search_type = sys.argv[2]
		return True

# checks/parses input file
def read_file():
	try:
   		with open(sys.argv[1]) as f:
   			env.create_matrix(f)
   			return True
   			
	except IOError:
   		print "Can't read file"
   		return False;

# Traslates PATH into readable movements
# acording to instructions in portuguese
# P = Get Gold, D = Right, E = Left, C = Up, B = Down
# Cost to pickup = +4 * size of environment
# Cost to move = -1
def translate_path(path):
	global env
	actions = []
	cost = 0
	while len(path) > 1:
		if path[0] in env.gold_locations:
			actions.append("P")
			cost = cost + 4 * int(env.size)
			if path[1] == path[0] + 1:
				actions.append("D")
				cost = cost - 1
			elif path[1] == path[0] - 1:
				actions.append("E")
				cost = cost - 1
			elif path[1] == path[0] + int(env.size):
				actions.append("B")
				cost = cost - 1
			elif path[1] == path[0] - int(env.size):
				actions.append("C")
				cost = cost - 1
		elif path[1] == path[0] + 1:
			actions.append("D")
			cost = cost - 1
		elif path[1] == path[0] - 1:
			actions.append("E")
			cost = cost - 1
		elif path[1] == path[0] + int(env.size):
			actions.append("B")
			cost = cost - 1
		elif path[1] == path[0] - int(env.size):
			actions.append("C")
			cost = cost - 1
		path.pop(0)
	print cost
	for c in actions:
		print c,

# main execution
if check_args():
	if read_file():
		if len(env.map) > 0:
			env.create_graph()

			if env.search_type == "L":
				a.track = []
				while env.gold_left:
				 	# initial pos
				 	state = a.current_state

				 	# objective state
				 	objective = env.gold_left[0]
				 	env.gold_left.pop(0)
					path = search.bfs(env.graph, state, objective, a)
					path.remove(path[len(path)-1])
					a.track.extend(path)

				# now go back to entrance
				path = search.bfs(env.graph, a.current_state, 0, a)
				a.track.extend(path)
				translate_path(a.track)

			if env.search_type == "P":
				print "Not Implemented"
