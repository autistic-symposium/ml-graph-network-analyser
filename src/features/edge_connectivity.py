import networkx as nx


def edgec(network):
    net = network.to_undirected()
    e = nx.edge_connectivity(net)
    return e


