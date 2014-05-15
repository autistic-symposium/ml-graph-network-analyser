'''
This script is called from each feature's database and process the feature vector values
'''

import networkx as nx

from save import save_feature

from features import   process_eccentricity, process_diameter, process_closeness,  process_between, process_ave_node_connectivity , process_density,  process_radius,  process_isolates, process_pagerank, process_square_clustering, process_communicability


def process_all_di(network, path_to_net, n, path_to_output):

  
	'''
        Features only defined for not dir graph:
        '''
	net = network.to_undirected(True) 
	#If True only keep edges that appear in both directions in the original digraph.

	'''
        Graph must be connected
	'''
        snet = nx.strongly_connected_component_subgraphs(network)
	try:
	        f, feature_name = process_eccentricity(snet[0], n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Eccentricity did not work!\n')
	try:
	        f, feature_name = process_diameter(snet[0], n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Diameter did not work!\n')
	try:
	        f, feature_name = process_closeness(network, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Closeness did not work!\n')
	try:
		f, feature_name = process_between(net, n, k=None)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Betweeness did not work!\n')
        try:
	        f, feature_name = process_density(network, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Density did not work!\n')
	try:	
	        f, feature_name = process_radius(snet[0], n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Radius did not work!\n')
	try:
	        f, feature_name = process_isolates(network, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Isolates did not work!\n')
	try:
	        f, feature_name = process_pagerank(network, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Pagerank did not work!\n')
	try:
	        f, feature_name = process_square_clustering(network, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Square clustering did not work!\n')
	try:
	        f, feature_name = process_communicability(net, n)
	        save_feature(path_to_output, f, feature_name, True)
	except:
		print('Communicability did not work!\n')	
	try:
		f, feature_name = process_ave_node_connectivity(net, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Node Connectivity did not work!\n') 





def process_all_un(network, path_to_net, n, path_to_output):

    	'''
        Need to connect components
	'''

	net = nx.connected_component_subgraphs(network)
	try:
	        f, feature_name = process_eccentricity(net[0], n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Eccentricity did not work!\n')
	try:
	        f, feature_name = process_diameter(net[0], n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Diameter did not work!\n')
	try:
	        f, feature_name = process_closeness(network, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Closeness did not work!\n')
	try:
		f, feature_name = process_between(net, n, k=None)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Betweeness did not work!\n')
        try:
	        f, feature_name = process_density(network, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Density did not work!\n')

        net = net[0].to_directed()
	try:	
	        f, feature_name = process_radius(net[0], n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Radius did not work!\n')

	try:
	        f, feature_name = process_isolates(network, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Isolates did not work!\n')
	try:
	        f, feature_name = process_pagerank(network, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Pagerank did not work!\n')
	try:
	        f, feature_name = process_square_clustering(network, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Square clustering did not work!\n')
	try:
	        f, feature_name = process_communicability(network, n)
	        save_feature(path_to_output, f, feature_name, True)
	except:
		print('Communicability did not work!\n')
	try:
		f, feature_name = process_ave_node_connectivity(net, n)
        	save_feature(path_to_output, f, feature_name)
	except:
		print('Node Connectivity did not work!\n') 	

