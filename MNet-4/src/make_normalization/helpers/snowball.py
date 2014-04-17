'''
Snowball sampling.

mari wahl @ 2014
'''

import networkx as nx
import random


def snowball_sampling(g, network, center, depth_sample=2, current_depth=0, sample_list=[]):

    g.add_node(center)
    neigh = network.neighbors(center)

    for i in range(len(neigh)): g.add_edge(center, neigh[i])

    if current_depth == depth_sample: return sample_list

    if center in sample_list: return sample_list

    else:
        for node in neigh:
            sample_list = snowball_sampling(g, network, node, depth_sample, current_depth+1, sample_list)
 
    return sample_list




def make_sample(network, depth_sample):
    center = random.choice(network.nodes())
    g = nx.DiGraph()

    snowball_sampling(g, network, center, depth_sample)
    
    return g
