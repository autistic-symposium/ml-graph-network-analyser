import networkx as nx
import snowball



def sampling_tar_dir(NETWORK_FILES, NUMBER_OF_NETWORKS, PATH_2_INPUT, TYPE_NET_DIR, NUM_SAMPLES, PATH_2_OUTPUT, DEPTH):

	for i, n in enumerate(NETWORK_FILES): 
		for j in range(NUMBER_OF_NETWORKS[i]):
		    path_to_input = PATH_2_INPUT + TYPE_NET_DIR + n + str(j) +'gpickle.1'
		    network = nx.read_gpickle(path_to_input) 
		    for r in range(NUM_SAMPLES):
		        path_to_output = PATH_2_OUTPUT + TYPE_NET_DIR + str(j) + n + str(r)  + '_SAMPLED_gpickle.1'
		        net = snowball.make_sample(network, DEPTH)
		        nx.write_gpickle(net, path_to_output)
			print("Sample " + str(r) + " generated at " + path_to_output)


def sampling_tar_un(NETWORK_FILES, NUMBER_OF_NETWORKS, PATH_2_INPUT, TYPE_NET_DIR, NUM_SAMPLES, PATH_2_OUTPUT, DEPTH):

	for i, n in enumerate(NETWORK_FILES): 
		for j in range(NUMBER_OF_NETWORKS[i]):
		    path_to_input = PATH_2_INPUT + TYPE_NET_DIR + n + str(j) +'gpickle.1'
		    network = nx.read_gpickle(path_to_input) 
		    for r in range(NUM_SAMPLES):
		        path_to_output = PATH_2_OUTPUT + TYPE_NET_DIR + str(j) + n + str(r)  + '_SAMPLED_gpickle.1'
		        net_sample = snowball.make_sample(network, DEPTH)

			net_sample.to_undirected()

		        nx.write_gpickle(net_sample, path_to_output)
			print("Sample " + str(r) + " generated at " + path_to_output)






def sampling_dir(NETWORK_FILES, PATH_2_INPUT, TYPE_NET_DIR, NUM_SAMPLES, PATH_2_OUTPUT, DEPTH):
    for n in NETWORK_FILES: 

        path_to_input = PATH_2_INPUT + TYPE_NET_DIR + n + 'gpickle.1'

        network = nx.read_gpickle(path_to_input) 
        
        for r in range(NUM_SAMPLES):
            path_to_output = PATH_2_OUTPUT + TYPE_NET_DIR + n + str(r) + '_SAMPLED_gpickle.1'
            net_sample = snowball.make_sample(network, DEPTH)
            nx.write_gpickle(net_sample, path_to_output)
	    print("Sample " + str(r) + " generated at " + path_to_output)



def sampling_un(NETWORK_FILES, PATH_2_INPUT, TYPE_NET_DIR, NUM_SAMPLES, PATH_2_OUTPUT, DEPTH):
    for n in NETWORK_FILES: 

        path_to_input = PATH_2_INPUT + TYPE_NET_DIR + n + 'gpickle.1'

        network = nx.read_gpickle(path_to_input) 
        
        for r in range(NUM_SAMPLES):
            path_to_output = PATH_2_OUTPUT + TYPE_NET_DIR + n + str(r) + '_SAMPLED_gpickle.1'
            net_sample = snowball.make_sample(network, DEPTH)
            net = net_sample.to_undirected()
            nx.write_gpickle(net, path_to_output)
	    print("Sample " + str(r) + " generated at " + path_to_output)

