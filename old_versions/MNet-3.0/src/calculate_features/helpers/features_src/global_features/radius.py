'''

The radius is the minimum eccentricity.
'''

import networkx as nx


def ra(network):
    d = 0
    for component in nx.strongly_connected_component_subgraphs(network):
    	d = nx.radius(component)
    return d

