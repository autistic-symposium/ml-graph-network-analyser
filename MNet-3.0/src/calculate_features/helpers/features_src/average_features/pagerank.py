'''

Return the PageRank of the nodes in the graph.

PageRank computes a ranking of the nodes in the graph G based on the structure of the incoming links. It was originally designed as an algorithm to rank web pages.


'''
import networkx as nx


def pg(network):
    p = nx.pagerank_numpy(network)
    m = sum(p.values())/len(p)
    return round(m, 5)
