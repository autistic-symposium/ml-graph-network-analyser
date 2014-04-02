import networkx as nx
from igraph import Graph

def gi(network):
    g = Graph.girth(network)
    print(g)
    return g


