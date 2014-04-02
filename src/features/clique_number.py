import networkx as nx


def clique(network):
    net = network.to_undirected()
    c = nx.graph_clique_number(net)

    return c
