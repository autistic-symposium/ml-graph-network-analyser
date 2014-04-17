'''
Return the diameter of the graph G.
'''

import networkx as nx


def diam(network):
    d = nx.diameter(network)
    return d

