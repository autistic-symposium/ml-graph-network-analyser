'''

Betweenness centrality of a node v is the sum of the fraction of all-pairs shortest paths that pass through v.

'''
import networkx as nx


def asp(network):
    c = nx.average_shortest_path_length(G)
    return c

