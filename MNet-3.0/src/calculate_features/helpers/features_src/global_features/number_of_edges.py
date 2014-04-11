'''
Total number of edges n the graph (graph size):
m = |E|
'''
import networkx as nx


def ne(network):
    m = network.number_of_edges()
    return m
