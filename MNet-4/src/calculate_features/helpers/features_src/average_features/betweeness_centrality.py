'''

Betweenness centrality of a node v is the sum of the fraction of all-pairs shortest paths that pass through v.

'''
import networkx as nx


def bc(network, k):
    c = nx.betweenness_centrality(network, k).values()
    m = sum(c)/len(c)
    return round(m, 5)

'''
def bc(network):
    b = nx.betweenness_centrality(network).items()
    r = [x[1] for x in b]
    m = sum(r)/len(r)
    return round(m, 3)
'''
