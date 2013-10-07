#
# MAC0425/5730 - Inteligencia Artificial - EP1 @ 2013.2
# Autor: Bruno Nunes Leal Faria - nUSP: 8765551
#
# FILE: main.py
#

import sys
import environment

# global var to hold environment variables
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
	x = 0
	y = 0
	try:
   		with open(sys.argv[1]) as f:
   			# read dimension
   			c = f.read(1)
   			# take not of gold mine size
   			env.size = c
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
							env.gold_count += 1
							env.gold_locations.append([y,x])
						mine_field[y][x] = c
						x += 1
   			else:
   				print "Not an integer or invalid range"
	except IOError:
   		print "Can't read file"
   		return False;
# main execution
if check_args():
	if read_file():
		if len(env.map) > 0:
			env.execute()


