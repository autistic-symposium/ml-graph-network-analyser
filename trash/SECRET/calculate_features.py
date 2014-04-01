import networkx as nx
import glob
from operator import itemgetter



def get_egos(directory):
    paths = glob.glob("%s/*.edges" % (directory,))
    egos = [int(x.split("/")[-1].split('.')[0]) for x in paths]
    return egos

def construct_network(ego, directory):
    fname = "%s/%d.edges" % (directory, ego)
    f = open(fname,'r')
    net = nx.DiGraph()
    for line in f:
        nodes = [int(x) for x in line.strip().split(' ')]
        [net.add_edge(ego, node) for node in nodes]
        net.add_edge(*nodes)
    f.close()
    return net
    

def process_feature_vectors(g):
    ave_node_connectivity =  nx.average_node_connectivity(g)		
    density = nx.density(g)
    return ave_node_connectivity, density


def main():
    network_raw__directories = ['twitter']
    for network_raw_type in network_raw__directories: 
	f = open('feature_' + network_raw_type + '.dat', 'a')
        egos = get_egos(network_raw_type)
        newtwors = [construct_network(ego, network_raw_type) for ego in egos]
        for single_newtwork in newtwors:
            ave_node_connectivity, density = process_feature_vectors(single_newtwork)
	    f.write(str(ave_node_connectivity) + ',')
	    f.write(str(density))	
        f.close()




if __name__ == '__main__':
    main()
