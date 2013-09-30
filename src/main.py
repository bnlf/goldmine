#
# MAC0425/5730 - Inteligencia Artificial - EP1 @ 2013.2
# Autor: Bruno Nunes Leal Faria - nUSP: 8765551
#
# FILE: main.py
#

import sys

# enviroment structure
# @map - multi dimensional array to hold mine map
# @agent - search type to execute
class environment:
	def __init__(self):
		self.map = [[]]
		self.agent = ""
		self.step_count = 0

# global var to hold environment variables
env = environment()

gold_pos = []

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
		env.agent = str(sys.argv[2])
		return True

# parses input file
def read_file():
	x = 0
	y = 0
	try:
   		with open(sys.argv[1]) as f:
   			# read dimension
   			c = f.read(1)
   			if c.isdigit():
   				mine_field = [[0]*int(c) for i in range(int(c))]
				# read newline
   				c = f.read(1) 
   				# read the mine map
   				while True:
					c = f.read(1)
					if not c or y > 7:
						# debug - resulting matrix
						# for x in range(8):
						# 	for y in range(8): 
						# 		print mine_field[x][y],
						# 	print "\n",
						env.map = mine_field
						return True
					elif c == "\n":
						y += 1
						x = 0
					else:
						# tracks gold in mine	
						if c == "*":
							gold_pos.append([y,x])
						elif c == "0":
							env.step_count += 1
						mine_field[y][x] = c
						x += 1
   			else:
   				print "Not an int or invalid range"
	except IOError:
   		print "Can't read file"
   		return False;

# moves the agent if possible
def agent_walk(pos_yx, actual_pos_y, actual_pos_x):
	# location destiny for the gold
	dest_x = pos_x[1]
	dest_y = pos_y[0]



	if check_step(pos_y, pos_x):
		c = env.map[pos_y, pos_x]
		# if gold, grab it
		if c == "*":
			env.map[pos_y, pos_x] = 0
			return True
		elif c == "0":
			env.map[pos_y, pos_x+1]

def check_step(pos_y, pos_x):
	valid = ["*", "0", "-1"]
	# if gold or free, continue this way
	if env.map[pos_y][pos_x] in valid:
		return True
	# if barrier, can't continue this way
	elif env.map[pos_y][pos_x] == "1":
		return False
	# unknown area, probably input error. Assume as barrier
	else:
		return False

# walks through the mine
def agent_harvest(mine_field):
	# tracks number of steps lefts
	steps_left = env.step_count

	# tracks number of gols
	has_gold = len(gold_pos)

	# counter 
	i = 0

	while has_gold > 0:
		# harvest gold until none is left
		if agent_walk(gold_pos[i], 0, 0):
			has_gold -= 1
			i += 1

# check input arguments before continuing
if check_args():
	# checks if input file is valid and parses it
	if read_file():
		if len(env.map) > 0:
			agent_harvest(env.map)

# print env.map
# print env.agent
# print gold_pos


