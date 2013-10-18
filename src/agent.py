#
# MAC0425/5730 - Inteligencia Artificial - EP1 @ 2013.2
# Autor: Bruno Nunes Leal Faria - nUSP: 8765551
#
# FILE: agent.py
#

# agent class
class agent:
	def __init__(self):
		# current position in the graph
		self.current_state = 0
		# steps returned from search algorithm
		self.track = []
