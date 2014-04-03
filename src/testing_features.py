import networkx as nx
import glob
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
    

def save_features(network, features):   
    file_feature = open('../features_vector/' + network + '.dat', 'w')
    for f in range(len(features[0])):
        for i in range(len(features)):
            file_feature.write(str(features[i][f]) + ' ')
        file_feature.write('\n') 
    file_feature.close()


def process_network(path):
    d_vector = []
    asso_vector = []
    bet_vector = []
    clique_vector = []
    clust_vector = []
    core_vector = []
    diam_vector = []
    dist_vector = []
    ecc_vector = []
    edgec_vector = []
    ex_vector = []
    gi_vector = []
    hc_vector = []
    vc_vector = []

    egos = get_egos(path)
    networks = [construct_network(ego, path) for ego in egos]
    for i, single_network in enumerate(networks):
        d = degree.d(single_network)
     	asso = assortivity.asso(single_network)
     	bet = betweeness.bet(single_network)
     	clique = clique_number.clique(single_network)
        clust = clustering_coefficent.clust(single_network)
        edgec = edge_connectivity.edgec(single_network) 
        vc = vertex_connectivity.vc_strong(single_network)
        core = None#coreness.core(single_network) --> to fix
        diam = None#diameter.diam(single_network)
        dist = None#distortion.dist(single_network) --> to fix
        ecc = None#eccentricity.ecc(single_network) --> to fix
        ex = None#expansion.ex(single_network) --> do it
        gi = None#girth.gi(single_network) --> do it
        hc = None#hop_count.hc(single_network)  --> do it

        d_vector.append(d)
        asso_vector.append(asso)
        bet_vector.append(bet)
        clique_vector.append(clique)
        clust_vector.append(clust)
        core_vector.append(core)
        diam_vector.append(diam)
        dist_vector.append(dist)
        ecc_vector.append(ecc)
        edgec_vector.append(edgec)
        ex_vector.append(ex)
        gi_vector.append(gi)
        hc_vector.append(hc)
        vc_vector.append(vc)

    return d_vector, asso_vector, bet_vector, clique_vector, clust_vector, edgec_vector, vc_vector,  core_vector, diam_vector, dist_vector, ecc_vector,  ex_vector, gi_vector, hc_vector



def main():
    path_to_data = "../data/raw_data/" 
    network_raw_directories = ["twitter"]	#add other directories or make this smarter

    for network_raw_type in network_raw_directories: 
        d, asso, bet, clique, clust, core, diam, dist, ecc, edgec, ex, gi, hc, vc = process_network(path_to_data+network_raw_type)
        save_features(network_raw_type, [d, asso, bet, clique, clust, core, diam, dist, ecc, edgec, ex, gi, hc, vc])





if __name__ == '__main__':
    main()
