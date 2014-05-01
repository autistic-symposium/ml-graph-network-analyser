import time

from features_src.global_features import assortativity, clique_number, number_of_cliques, number_of_edges, number_of_nodes, transitivity, radius, isolates, edge_connectivity, diameter, density, node_connectivity, clustering

from features_src.average_features import betweeness_centrality, coreness, degree_centrality, closeness_centrality, communicability_centrality, eccentricity, number_of_triangles, square_clustering, pagerank,  shortest_path_leng


def process_between(net, net_name, k=None):
    feature_name = "Betweeness"
    print("Calculating " + feature_name + " for " + net_name + "...")
    f =  betweeness_centrality.bc(net, k)
    print("Done! Time: " + time.strftime("%I:%M:%S"))
    return str(f), feature_name 


def process_degree(net, net_name):
    feature_name = "Degree"
    print("Calculating " + feature_name + " for " + net_name + "...")
    f = degree_centrality.dc(net)
    print("Done! Time: " + time.strftime("%I:%M:%S"))
    return str(f), feature_name 


def process_coreness(net, net_name):
    feature_name = "Coreness"
    print("Calculating " + feature_name + " for " + net_name + "...")
    f =  coreness.core(net)
    print("Done! Time: " + time.strftime("%I:%M:%S"))
    return str(f), feature_name 


def process_assortativity(net, net_name):
    feature_name = "Assortativity"
    print("Calculating " + feature_name + " for " + net_name + "...")
    f =  assortativity.asso(net)
    print("Done! Time: " + time.strftime("%I:%M:%S"))
    return str(f), feature_name 


def process_order(net, net_name):
    feature_name = "Order"
    print("Calculating " + feature_name + " for " + net_name + "...")
    f =  number_of_edges.ne(net)
    print("Done! Time: " + time.strftime("%I:%M:%S"))
    return str(f), feature_name 


def process_size(net, net_name):
    feature_name = "Size"
    print("Calculating " + feature_name + " for " + net_name + "...")
    f =  number_of_nodes.nn(net)
    print("Done! Time: " + time.strftime("%I:%M:%S"))
    return str(f), feature_name 


def process_number_cliques(net, net_name):
    feature_name = "Num_Cliques"
    print("Calculating " + feature_name + " for " + net_name + "...")
    f =  number_of_cliques.nc(net)
    print("Done! Time: " + time.strftime("%I:%M:%S"))
    return str(f), feature_name 


def process_transitivity(net, net_name):
    feature_name = "Transitivity"
    print("Calculating " + feature_name + " for " + net_name + "...")
    f =  transitivity.trans(net)
    print("Done! Time: " + time.strftime("%I:%M:%S"))
    return str(f), feature_name 


def process_clique_number(net, net_name):
    feature_name = "Clique_Number"
    print("Calculating " + feature_name + " for " + net_name + "...")
    f =  clique_number.cn(net)
    print("Done! Time: " + time.strftime("%I:%M:%S"))
    return str(f), feature_name 


def process_closeness(net, net_name):
    feature_name = "Closeness"
    print("Calculating " + feature_name + " for " + net_name + "...")
    f =  closeness_centrality.cc(net)
    print("Done! Time: " + time.strftime("%I:%M:%S"))
    return str(f), feature_name 

def process_clustering(net, net_name):
    feature_name = "Clustering"
    print("Calculating " + feature_name + " for " + net_name + "...")
    f = clustering.clust(net)
    print("Done! Time: " + time.strftime("%I:%M:%S"))
    return str(f), feature_name 

def process_communicability(net, net_name):
    feature_name = "Communicability"
    print("Calculating " + feature_name + " for " + net_name + "...")
    f = communicability_centrality.cc(net)
    print("Done! Time: " + time.strftime("%I:%M:%S"))
    return str(f), feature_name 


def process_eccentricity(net, net_name):
    feature_name = "Eccentricity"
    print("Calculating " + feature_name + " for " + net_name + "...")
    f = eccentricity.ecc(net)
    print("Done! Time: " + time.strftime("%I:%M:%S"))
    return str(f), feature_name 

def process_num_triangles(net, net_name):
    feature_name = "Num_Triangles"
    print("Calculating " + feature_name + " for " + net_name + "...")
    f = number_of_triangles.nt(net)
    print("Done! Time: " + time.strftime("%I:%M:%S"))
    return str(f), feature_name 

def process_pagerank(net, net_name):
    feature_name = "Pagerank"
    print("Calculating " + feature_name + " for " + net_name + "...")
    f = pagerank.pg(net)
    print("Done! Time: " + time.strftime("%I:%M:%S"))
    return str(f), feature_name 

def process_square_clustering(net, net_name):
    feature_name = "Square_clust"
    print("Calculating " + feature_name + " for " + net_name + "...")
    f = square_clustering.sclust(net)
    print("Done! Time: " + time.strftime("%I:%M:%S"))
    return str(f), feature_name 

def process_radius(net, net_name):
    feature_name = "Radius"
    print("Calculating " + feature_name + " for " + net_name + "...")
    f = radius.ra(net)
    print("Done! Time: " + time.strftime("%I:%M:%S"))
    return str(f), feature_name 

def process_isolates(net, net_name):
    feature_name = "Isolates"
    print("Calculating " + feature_name + " for " + net_name + "...")
    f = isolates.iso(net)
    print("Done! Time: " + time.strftime("%I:%M:%S"))
    return str(f), feature_name 

def process_diameter(net, net_name):
    feature_name = "Diameter"
    print("Calculating " + feature_name + " for " + net_name + "...")
    f = diameter.diam(net)
    print("Done! Time: " + time.strftime("%I:%M:%S"))
    return str(f), feature_name 

def process_density(net, net_name):
    feature_name = "Density"
    print("Calculating " + feature_name + " for " + net_name + "...")
    f = density.den(net)
    print("Done! Time: " + time.strftime("%I:%M:%S"))
    return str(f), feature_name 

def process_ave_node_connectivity(net, net_name):
    feature_name = "Ave_Node_conn"
    print("Calculating " + feature_name + " for " + net_name + "...")
    f = node_connectivity.anc(net)
    print("Done! Time: " + time.strftime("%I:%M:%S"))
    return str(f), feature_name 


def process_edge_connectivity(net, net_name):
    feature_name = "Edge_conn"
    print("Calculating " + feature_name + " for " + net_name + "...")
    f = edge_connectivity.ec(net)
    print("Done! Time: " + time.strftime("%I:%M:%S"))
    return str(f), feature_name 

def process_node_connectivity(net, net_name):
    feature_name = "Node_conn"
    print("Calculating " + feature_name + " for " + net_name + "...")
    f = node_connectivity.nc(net)
    print("Done! Time: " + time.strftime("%I:%M:%S"))
    return str(f), feature_name 

    return str(f), feature_name 

def process_shortest_path_leng(net, net_name):
    feature_name = "Ave Shortest Path"
    print("Calculating " + feature_name + " for " + net_name + "...")
    f = shortest_path_leng.asp(net)
    print("Done! Time: " + time.strftime("%I:%M:%S"))
    return str(f), feature_name 