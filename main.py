#
# MAC0425/5730 - Inteligencia Artificial - EP1 @ 2013.2
# Autor: Bruno Nunes Leal Faria - nUSP: 8765551
#
# FILE: main.c
#

import sys

# enviroment structure
# @map - multi dimensional array to hold mine map
# @agent - search type to execute
class enviroment:
	def __init__(self):
		self.map = [[]]
		self.agent = ""

# global var to hold enviroment variables
env = enviroment()

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
						break
					elif c == "\n":
						y = y + 1
						x = 0
					else:	
						mine_field[y][x] = c
						x = x + 1
   			else:
   				print "Not an int or invalid range"
	except IOError:
   		print "Can't read file"
   		return False;

# check input arguments before continuing
check_args()

# checks if input file is valid and parses it
read_file()

print env.map
print env.agent


