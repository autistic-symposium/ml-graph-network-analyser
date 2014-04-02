import networkx as nx


def diam(network):
    # The diameter is the maximum eccentricity.
    d = nx.diameter(network)
    return d


