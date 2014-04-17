'''
Compute the average clustering coefficient for the graph G.
'''

import networkx as nx

def clust(network):
    c = nx.average_clustering(network, count_zeros=False)
    return round(c, 3)



