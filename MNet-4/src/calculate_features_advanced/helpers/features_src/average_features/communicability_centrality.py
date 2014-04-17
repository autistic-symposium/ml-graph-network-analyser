'''
Communicability centrality, also called subgraph centrality, of a node n is the sum of closed walks of all lengths starting and ending at node n.

Communicability centrality of a node u in G can be found using a spectral decomposition of the adjacency matrix. 

'''
import networkx as nx


def cc(net):
    c = nx.communicability_centrality(net)
    m = sum(c.values())/len(c)
    return round(m, 5)
