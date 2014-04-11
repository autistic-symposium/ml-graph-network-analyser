'''
Isolates are nodes with no neighbors (degree zero).
'''

import networkx as nx


def iso(network):
    i = nx.isolates(network)
    return i


