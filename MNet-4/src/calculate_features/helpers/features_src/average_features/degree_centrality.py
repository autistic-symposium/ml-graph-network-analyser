'''
The degree centrality of a node v is the fraction of nodes it is connected to.

The degree centrality values are normalized by dividing by the maximum possible degree in a simple graph n-1 where n is the number of nodes in G.

For multigraphs or graphs with self loops the maximum degree might be higher than n-1 and values of degree centrality greater than 1 are possible.
'''

import networkx as nx


def dc(net):
    if len(net) < 1: 
	print('\nLENGHT OF DEGREE CENTRALITY IS O!!!')
        return 0
    d = nx.degree_centrality(net)
    if len(d) == 0: 
	print('\nLENGHT OF DEGREE CENTRALITY IS O!!!')
        return 0
    else:
	m = sum(d.values())/len(d.values())
    	return round(m, 5)


