'''
mhrw sampling.

mari wahl @ 2014
'''

import networkx as nx
import random


def mhrw_sampling(g, network, size, count): 

    v = random.choice(network.nodes())
    sample = [v]  
    g.add_node(v)


    while len(sample) < size:
        neighbors = nx.neighbors(network, v)
        if not neighbors: 
	    print('\n NO NEIGHBORS! Count: %d'%(count))
            return False
        vnew = random.choice(neighbors) 
        vold = v
        v = vnew if (random.random() <float(network.degree(v))/network.degree(vnew)) else v
        sample.append(v)
        g.add_edge(v, vold)  #for i in range(len(neighbors)): g.add_edge(v, neighbors[i])
    print('\n WORKED!')
    return True
        


      
    


def make_sample(network, depth_sample):
    g = nx.DiGraph()
    worked = False
    count = 0
    size = 1000
    while worked == False and count < size:
        worked = mhrw_sampling(g, network, size, count)
        count += 1

    if count == size:
	print("\n I'M AFFRAID IT DIDN'T WORK, JAMES")
        g = network

    return g





