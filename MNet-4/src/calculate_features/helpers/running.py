import networkx as nx
import process

def running_un(NETWORK_FILES_UN, NUM_SAMPLES, PATH_2_GRAPHS, TYPE_NET_DIR, PATH_2_OUTPUT):
    for n in NETWORK_FILES_UN: 
	for r in range(NUM_SAMPLES):
            path_to_net = PATH_2_GRAPHS + TYPE_NET_DIR + n +  str(r) + '_SAMPLED_gpickle.1'
            path_to_output = PATH_2_OUTPUT + TYPE_NET_DIR + n +  str(r) + '_VECTOR_SAMPLED.dat'

            network = nx.read_gpickle(path_to_net) 
            process.process_all_un(network, path_to_net, n, path_to_output)

            print("All feature saved in the output file: " +  path_to_output + '\n')


def running_dir(NETWORK_FILES_DIR, NUM_SAMPLES, PATH_2_GRAPHS, TYPE_NET_DIR, PATH_2_OUTPUT):
    for n in NETWORK_FILES_DIR: 
	for r in range(NUM_SAMPLES):
            path_to_net = PATH_2_GRAPHS + TYPE_NET_DIR + n +  str(r) + '_SAMPLED_gpickle.1'
            path_to_output = PATH_2_OUTPUT + TYPE_NET_DIR + n + str(r) + '_VECTOR_SAMPLED.dat'

            network = nx.read_gpickle(path_to_net) 
            process.process_all_di(network, path_to_net, n, path_to_output)

            print("All feature saved in the output file: " +  path_to_output + '\n')


def running_un_tar(NETWORK_FILES_UN, NUMBER_OF_NETWORKS_UN, NUM_SAMPLES, PATH_2_GRAPHS, TYPE_NET_DIR, PATH_2_OUTPUT):
    for i,n in enumerate(NETWORK_FILES_UN): 
	for j in range(NUMBER_OF_NETWORKS_UN):
            for r in range(NUM_SAMPLES):
		path_to_net = PATH_2_GRAPHS + TYPE_NET_DIR + str(j) + n + str(r) + '_SAMPLED_gpickle.1'
		path_to_output = PATH_2_OUTPUT + TYPE_NET_DIR + str(j) + n + str(r) + '_VECTOR_SAMPLED.dat'

		network = nx.read_gpickle(path_to_net) 
		process.process_all_un(network, path_to_net, n, path_to_output)

		print("All feature saved in the output file: " +  path_to_output + '\n')


def running_dir_tar(NETWORK_FILES_DIR, NUMBER_OF_NETWORKS_DIR, NUM_SAMPLES, PATH_2_GRAPHS, TYPE_NET_DIR, PATH_2_OUTPUT):
    for i, n in enumerate(NETWORK_FILES_DIR): 
	num_net_here = NUMBER_OF_NETWORKS_DIR[i]
        for j in range(num_net_here):
            for r in range(NUM_SAMPLES):
		path_to_net = PATH_2_GRAPHS + TYPE_NET_DIR + str(j) + n + str(r) +  '_SAMPLED_gpickle.1'
		path_to_output = PATH_2_OUTPUT + TYPE_NET_DIR +str(j) + n + str(r) +  '_VECTOR_SAMPLED.dat'

		network = nx.read_gpickle(path_to_net) 
		process.process_all_di(network, path_to_net, n, path_to_output)

		print("All feature saved in the output file: " +  path_to_output + '\n')
