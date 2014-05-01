'''
This script is called from each feature's database and process the feature vector values
'''

import networkx as nx
import sys

from save import save_feature

from features import   process_order, process_size, process_assortativity, process_transitivity, process_degree, process_coreness, process_num_triangles, process_number_cliques, process_clique_number, process_clustering,  process_edge_connectivity


def process_all_di(network, path_to_net, n, path_to_output):

        try:
	        f, feature_name = process_size(network, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Size did not work!')
	try:	
	        f, feature_name = process_order(network, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Order did not work!')
	try:
	        f, feature_name = process_assortativity(network, n)
        	save_feature(path_to_output, f, feature_name) 
	except:
		print('Assortativity did not work!')
	try:
	        f, feature_name = process_transitivity(network, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Transitivity did not work!')
	try:
	        f, feature_name = process_degree(network, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Degree did not work!')
	try:
	        f, feature_name = process_coreness(network, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Coreness did not work!')
	
	'''
        Features only defined for not dir graph:
        '''
	net = network.to_undirected(True) 
	#If True only keep edges that appear in both directions in the original digraph.
	try:
	        f, feature_name = process_num_triangles(net, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Number of triangles did not work!')
	try:
	        f, feature_name = process_number_cliques(net, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Number of cliques did not work!')
	try:
	        f, feature_name = process_clique_number(net, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Clique number did not work!')
	try:
	        f, feature_name = process_clustering(net, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Clustering did not work!')
	try:
	        f, feature_name = process_edge_connectivity(net, n)
        	save_feature(path_to_output, f, feature_name, True)
	except:
		print('Edge connecticity did not work!')
	




def process_all_un(network, path_to_net, n, path_to_output):
	try:
	        f, feature_name = process_size(network, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Number triangles did not work.\n')
	try:
	        f, feature_name = process_order(network, n)
        	stave_feature(path_to_output, f, feature_name)
	except:
		print('Order did not work.\n')
	try:
	        f, feature_name = process_assortativity(network, n)
        	save_feature(path_to_output, f, feature_name) 
	except:
		print('Assortativity did not work.\n')
	try:
	        f, feature_name = process_transitivity(network, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Transitivity did not work.\n')
	try:
	        f, feature_name = process_degree(network, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Degree did not work.\n')
	try:
	        f, feature_name = process_coreness(network, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Coreness did not work.\n')
	try:
	        f, feature_name = process_num_triangles(network, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Number of Triangles did not work.\n')
	try:
	        f, feature_name = process_number_cliques(network, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Process number did not work.\n')
	try:
	        f, feature_name = process_clique_number(network, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Clique number did not work.\n')
	try:
	        f, feature_name = process_clustering(network, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Clustering did not work.\n')
	try:
	        f, feature_name = process_edge_connectivity(network, n)
        	save_feature(path_to_output, f, feature_name, True)
	except:
		print('Edge connectivity did not work.\n')


	




