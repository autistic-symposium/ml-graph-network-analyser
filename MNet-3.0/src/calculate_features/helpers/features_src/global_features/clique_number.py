'''
Return the clique number (size of the largest clique) for G.
'''

import networkx as nx


def cn(network):
    c = nx.graph_clique_number(network)
    return c
