import networkx as nx
import glob
import matplotlib.pyplot as plt
import os
import pickle
from features import degree, assortivity, betweeness,clique_number, clustering_coefficent, coreness, diameter, distortion, eccentricity, edge_connectivity, expansion, girth, hop_count, vertex_connectivity



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
    

def save_features(features):
    print(features)


def process_network(path):
    fea = []
    egos = get_egos(path)
    networks = [construct_network(ego, path) for ego in egos]
    for i, single_network in enumerate(networks):
        d = degree.d(single_network)
     	asso = assortivity.asso(single_network)
     	bet = betweeness.bet(single_network)
     	clique = clique_number.clique(single_network)
        clust = clustering_coefficent.clust(single_network)
        core = coreness.core(single_network)
        diam = diameter.diam(single_network)
        dist = distortion.dist(single_network)
        ecc = eccentricity.ecc(single_network)
        edgec = edge_connectivity.edgec(single_network)
        ex = expansion.ex(single_network)
        gi = girth.gi(single_network)
        hc = hop_count.hc(single_network)
        vc = vertex_connectivity.vc(single_network)

        fea.append([d, asso, bet, clique, clust, core, diam, dist, ecc, edgec, ex, gi, hc, vc])

    return fea



def main():
    path_to_data = "./data/raw_data/" 
    network_raw_directories = ["twitter"]	#add other directories or make this smarter

    for network_raw_type in network_raw_directories: 
        fea = process_network(path_to_data+network_raw_type)
    
    save_features(fea)





if __name__ == '__main__':
    main()
