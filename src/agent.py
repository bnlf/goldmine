#
# MAC0425/5730 - Inteligencia Artificial - EP1 @ 2013.2
# Autor: Bruno Nunes Leal Faria - nUSP: 8765551
#
# FILE: agent.py
#

# Depth First Search
# @Dict graph
# @Lambda fn
# @List visited
def _visit(graph, fn, visited):
    for node, adj in sorted(graph.items()):
        if node not in visited:
            visited.append(node)
            fn(node)
            _visit(graph[node], fn, visited)

# @Integer node
# @Dict graph
# @Lambda fn
def visit(node, graph, fn):
    _visit({node:graph[node]}, fn, [])