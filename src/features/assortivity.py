import networkx as nx


def asso(network):
    return nx.degree_assortativity_coefficient(network)


