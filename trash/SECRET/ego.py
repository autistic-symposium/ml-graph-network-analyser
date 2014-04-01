import networkx as nx
import numpy as np
import glob
from operator import itemgetter
import matplotlib.pyplot as plt
import snap

datadir = 'raw'

def get_egos():
    paths = glob.glob("%s/*.edges" % (datadir,))
    egos = [int(x.split("/")[-1].split('.')[0]) for x in paths]
    return egos

def construct_network(ego):
    fname = "%s/%d.edges" % (datadir, ego)
    f = open(fname,'r')
    net = nx.DiGraph()
    for line in f:
        nodes = [int(x) for x in line.strip().split(' ')]
        [net.add_edge(ego, node) for node in nodes]
        net.add_edge(*nodes)
    f.close()
    return net
    

def ego_graph(graph):
    # Create a BA model graph
    n=1000
    m=2
    G=nx.generators.barabasi_albert_graph(n,m)
    # find node with largest degree
    node_and_degree=G.degree()
    (largest_hub,degree)=sorted(node_and_degree.items(),key=itemgetter(1))[-1]
    # Create ego graph of main hub
    hub_ego=nx.ego_graph(G,largest_hub)
    # Draw graph
    pos=nx.spring_layout(hub_ego)
    nx.draw(hub_ego,pos,node_color='b',node_size=50,with_labels=False)
    # Draw ego as large and red
    nx.draw_networkx_nodes(hub_ego,pos,nodelist=[largest_hub],node_size=300,node_color='r')
    plt.savefig('ego_graph.png')
    plt.show()


def centrality(G):


	print("Betweenness")
	b=nx.betweenness_centrality(G)
	for v in G.nodes():
	    print("%0.2d %5.3f"%(v,b[v]))

	print("Degree centrality")
	d=nx.degree_centrality(G)
	for v in G.nodes():
	    print("%0.2d %5.3f"%(v,d[v]))

	print("Closeness centrality")
	c=nx.closeness_centrality(G)
	for v in G.nodes():
	    print("%0.2d %5.3f"%(v,c[v]))


def random_geometric_graph(graph):
	G=nx.random_geometric_graph(200,0.125)
	# position is stored as node attribute data for random_geometric_graph
	pos=nx.get_node_attributes(G,'pos')

	# find node near center (0.5,0.5)
	dmin=1
	ncenter=0
	for n in pos:
	    x,y=pos[n]
	    d=(x-0.5)**2+(y-0.5)**2
	    if d<dmin:
		ncenter=n
		dmin=d

	# color by path length from node near center
	p=nx.single_source_shortest_path_length(G,ncenter)

	plt.figure(figsize=(8,8))
	nx.draw_networkx_edges(G,pos,nodelist=[ncenter],alpha=0.4)
	nx.draw_networkx_nodes(G,pos,nodelist=p.keys(),
		               node_size=80,
		               node_color=p.values(),
		               cmap=plt.cm.Reds_r)

	plt.xlim(-0.05,1.05)
	plt.ylim(-0.05,1.05)
	plt.axis('off')
	plt.savefig('random_geometric_graph.png')
	plt.show()

def process(adjacency=True):
    egos = get_egos()
    networks = [construct_network(ego) for ego in egos]
    if adjacency:
        max_nodes = max([n.number_of_nodes() for n in networks])
        X = np.zeros((len(networks), max_nodes**2))
        for i,network in enumerate(networks):
            X[i] = np.resize(nx.adjacency_matrix(network), max_nodes**2) #network.number_of_nodes()**2)
        return X
    else:
        return networks


def main():
	#graph = (process(adjacency=True))
    	egos = get_egos()
    	graph = [construct_network(ego) for ego in egos]
        #ego_graph(graph)
        #random_geometric_graph(graph)
	#cf = snap.GetClustCf(graph)
	#G7 = snap.ConvertGraph(snap.PUNGraph, graph)
	#print "G7: Nodes %d, Edges %d" % (G7.GetNodes(), G7.GetEdges())
  	# get largest weakly connected component
	#WccG = snap.GetMxWcc(G6)
	v = snap.TIntV()

	v.Add(1)
	v.Add(2)
	v.Add(3)
	v.Add(4)
	v.Add(5)

	print v.Len()
	print v[2]

	#centrality(graph)
	for g in graph:	
		print(nx.average_node_connectivity(g))		
		print(nx.density(g))
		#print(sorted(nx.degree(g)))	
                #centrality(g)	
		#print(sorted(nx.degree(g)))	


if __name__ == '__main__':
    main()
