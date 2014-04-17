'''
The degree centrality of a node v is the fraction of nodes it is connected to.

The degree centrality values are normalized by dividing by the maximum possible degree in a simple graph n-1 where n is the number of nodes in G.

For multigraphs or graphs with self loops the maximum degree might be higher than n-1 and values of degree centrality greater than 1 are possible.
'''

import networkx as nx


def dc (net):
    d = nx.degree_centrality(net).values()
    m = sum(d)/len(d)
    return round(m, 5)


