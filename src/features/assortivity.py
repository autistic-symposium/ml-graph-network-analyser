import networkx as nx


def asso(network):
    a = nx.degree_assortativity_coefficient(network)
    return round(a, 3)

