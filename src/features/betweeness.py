import networkx as nx


def bet(network):
    net = network.to_undirected()
    #net_mc = nx.connected_component_subgraphs(net)
    b = nx.betweenness_centrality(net).items()
    r = [x[1] for x in b]
    # mean centrality
    m = sum(r)/len(r)
    return round(m, 3)

