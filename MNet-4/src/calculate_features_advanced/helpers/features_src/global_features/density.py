'''
Return the density of a graph.
'''

import networkx as nx


def den(network):
    d = nx.density(network)
    return d


