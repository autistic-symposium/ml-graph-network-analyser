import networkx as nx


def core(network):
    net = network.to_undirected()
    net_mc = nx.connected_component_subgraphs(net)
    #print(net_mc)
    c = nx.core_number(net_mc).items()
    r = [x[1] for x in c]
    # mean core_number
    m = sum(r)/len(r)
    return round(m, 3)


