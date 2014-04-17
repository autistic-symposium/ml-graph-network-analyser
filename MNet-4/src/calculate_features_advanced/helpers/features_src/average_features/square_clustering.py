'''
Compute the squares clustering coefficient for nodes: the fraction of possible squares that exist at the node.

'''


import networkx as nx

def sclust(network):
    c = nx.square_clustering(network)
    m = sum(c.values())/len(c)
    return round(m, 5)



