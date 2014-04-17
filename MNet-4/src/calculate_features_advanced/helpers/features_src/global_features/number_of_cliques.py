'''
Returns the number of maximal cliques in G.
'''

import networkx as nx


def nc(network):
    c = nx.graph_number_of_cliques(network)
    return c
