'''
Compute graph transitivity, the fraction of all possible triangles present in G.

'''

import networkx as nx


def trans(network):
    t = nx.transitivity(network)
    return round(t, 3)
