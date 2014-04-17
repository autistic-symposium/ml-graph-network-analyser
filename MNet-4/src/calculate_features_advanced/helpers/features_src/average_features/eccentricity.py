'''

The eccentricity of a node v is the maximum distance from v to all other nodes in G.
'''

import networkx as nx


def ecc(network):
	e = nx.eccentricity(network).values()
	m = sum(e)/len(e)
	return round(m, 3)
