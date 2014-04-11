
'''
Node connectivity is equal to the minimum number of nodes that must be removed to disconnect G or render it trivial. If source and target nodes are provided, this function returns the local node connectivity.

Returns the average connectivity of a graph G.
'''

import networkx as nx


def anc(network):
    n = nx.average_node_connectivity(network)
    return round(n, 3)

'''
Returns node connectivity for a graph or digraph G.

'''

def nc(network):
    n = nx.node_connectivity(network)
    return n
