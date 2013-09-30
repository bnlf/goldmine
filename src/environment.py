#
# MAC0425/5730 - Inteligencia Artificial - EP1 @ 2013.2
# Autor: Bruno Nunes Leal Faria - nUSP: 8765551
#
# FILE: environment.py
#

# enviroment structure
# @map - multi dimensional array to hold mine map
# @agent - search type to execute
class environment:
	def __init__(self):
		self.map = [[]]
		self.agent = ""