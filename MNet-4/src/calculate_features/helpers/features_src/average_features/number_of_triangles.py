'''

Finds the number of triangles that include a node as one vertex.
'''

import networkx as nx


def nt(network):
    c = nx.triangles(network)
    m = sum(c.values())/len(c)
    return round(m, 5)

