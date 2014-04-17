''' 
Assortativity measures the similarity of connections in the graph with respect to the node degree.

Associative mixing by degree can be quantified in a number of ways, one of them is to use the correlation coefficient.

Graphs that have only single edges between vertices tend in the absence of other biases to show disassortative mixing by degree because the number of edges that can fall between high-degree vertex pairs is limited. Since most networks are represented as simple graphs this implies that most should be disassortative.

'''

import networkx as nx


def asso(network):
    a = nx.degree_pearson_correlation_coefficient(network)
    return round(a, 3)

