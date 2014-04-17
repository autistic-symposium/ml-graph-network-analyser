'''
Return the core number for each vertex.

A k-core is a maximal subgraph that contains nodes of degree k or more.

The core number of a node is the largest value k of a k-core containing that node.
'''

import networkx as nx


def core(net):
    if net.number_of_selfloops() > 0: 
        net.remove_edges_from(net.selfloop_edges())
    c = nx.core_number(net).values()
    m = sum(c)/len(c)
    return round(m, 5)


