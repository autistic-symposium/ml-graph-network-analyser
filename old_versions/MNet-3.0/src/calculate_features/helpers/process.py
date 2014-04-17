'''
This script is called from each feature's database and process the feature vector values
'''

import networkx as nx

from save import save_feature

from features import   process_order, process_size, process_assortativity, process_transitivity, process_degree, process_coreness, process_num_triangles, process_number_cliques, process_clique_number, process_clustering,  process_edge_connectivity


def process_all_di(network, path_to_net, n, path_to_output):

        f, feature_name = process_size(network, n)
        save_feature(path_to_output, f, feature_name)

        f, feature_name = process_order(network, n)
        save_feature(path_to_output, f, feature_name)

        f, feature_name = process_assortativity(network, n)
        save_feature(path_to_output, f, feature_name) 

        f, feature_name = process_transitivity(network, n)
        save_feature(path_to_output, f, feature_name)
	
        f, feature_name = process_degree(network, n)
        save_feature(path_to_output, f, feature_name)

        f, feature_name = process_coreness(network, n)
        save_feature(path_to_output, f, feature_name)

	'''
        Features only defined for not dir graph:
        '''
	net = network.to_undirected(True) 
	#If True only keep edges that appear in both directions in the original digraph.

        f, feature_name = process_num_triangles(net, n)
        save_feature(path_to_output, f, feature_name)

        f, feature_name = process_number_cliques(net, n)
        save_feature(path_to_output, f, feature_name)
	
        f, feature_name = process_clique_number(net, n)
        save_feature(path_to_output, f, feature_name)

        f, feature_name = process_clustering(net, n)
        save_feature(path_to_output, f, feature_name)

        f, feature_name = process_edge_connectivity(net, n)
        save_feature(path_to_output, f, feature_name)






def process_all_un(network, path_to_net, n, path_to_output):

        f, feature_name = process_size(network, n)
        save_feature(path_to_output, f, feature_name)

        f, feature_name = process_order(network, n)
        save_feature(path_to_output, f, feature_name)

        f, feature_name = process_assortativity(network, n)
        save_feature(path_to_output, f, feature_name) 

        f, feature_name = process_transitivity(network, n)
        save_feature(path_to_output, f, feature_name)
	
        f, feature_name = process_degree(network, n)
        save_feature(path_to_output, f, feature_name)
	
        f, feature_name = process_coreness(network, n)
        save_feature(path_to_output, f, feature_name)

        f, feature_name = process_num_triangles(network, n)
        save_feature(path_to_output, f, feature_name)
	
        f, feature_name = process_number_cliques(network, n)
        save_feature(path_to_output, f, feature_name)

        f, feature_name = process_clique_number(network, n)
        save_feature(path_to_output, f, feature_name)

        f, feature_name = process_clustering(network, n)
        save_feature(path_to_output, f, feature_name)

        f, feature_name = process_edge_connectivity(network, n)
        save_feature(path_to_output, f, feature_name)


	




