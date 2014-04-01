import networkx as nx
import glob
import matplotlib.pyplot as plt
import os
import pickle

from features import *

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
    

def process_network(network_raw_type):
        egos = get_egos(network_raw_type)
        newtworks = [construct_network(ego, network_raw_type) for ego in egos]
        for i, single_newtwork in enumerate(newtworks):
            n = nx.number_of_nodes(single_newtwork)
            dd = nx.density(single_newtwork)
            a = nx.degree_assortativity_coefficient(single_newtwork)
            print(str(dd) + ',' + str(n))
            #nx.write_gpickle(single_newtwork, network_raw_type + "/graphs/" +"graph_" + str(i) + ".gpickle")
        


def process_features(g):
    d=nx.degree_centrality(g) 
    b=nx.betweenness_centrality(g)
    c=nx.closeness_centrality(g)
    cc =  nx.average_node_connectivity(g)		
    dd = nx.density(g)
    a = nx.degree_assortativity_coefficient(g)
    # find maximum number of clique
    #max_clique = nx.max_clique(g)
    #e = nx.eccentricity(g)
    #diam = nx.diameter(g)
    n = nx.number_of_nodes(g)
    k = nx.number_of_edges(g)
    core = nx.core_number(g)
    ec = nx.edge_connectivity(g)
    print(cc, n)
    #print( str(round(cc,2)), str(round(dd,2)),str(round(a,2)))

def process_feature_vectors(graph_file, graphs_path):
    graph_path = graphs_path + graph_file
    g = nx.read_gpickle(graph_path)
    features_this_graph = process_features(g)
    

    return features_this_graph 



def main():
    network_raw__directories = ['twitter']
    for network_raw_type in network_raw__directories: 
        process_network(network_raw_type)
    
    for network_raw_type in network_raw__directories:
        graphs_path = "./twitter/graphs/"
        list_dir = []
        list_dir = os.listdir(graphs_path)




if __name__ == '__main__':
    main()
