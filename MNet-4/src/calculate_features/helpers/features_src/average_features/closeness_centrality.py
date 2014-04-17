'''
Closeness centrality at a node is 1/average distance to all other nodes.

The closeness centrality is normalized to to n-1 / size(G)-1 where n is the number of nodes in the connected part of graph containing the node. If the graph is not completely connected, this algorithm computes the closeness centrality for each connected part separately.

It measures how fast information spreads from a given node to other reachable nodes in the graphs. For a node $u$, it represents the reciprocal of the average shortest path length between $u$ and every other reachable node in the graph:

'''
import networkx as nx


def cc(network):
    c = nx.closeness_centrality(network)
    m = sum(c.values())/len(c)
    return round(m, 5)





'''
def cc(network):
    c= nx.closeness_centrality(network).items()
    r = [x[1] for x in c]
    m = sum(r)/len(r)
    return round(m, 3)
'''

