MNet - Network Analysis Package
===============================

Extraction and analysis of several graph features from publicly available datasets using NetworkX.

Features Analyzed:
------------------
* Eccentricity
* Diameter
* Girth
* Expansion
* Betweeness
* Hop counts
* Distortion
* Degree
* Assortivity
* Coreness
* Clique number
* Clustering coefficient
* Vertex connectivity
* Edge connectivity

Features from the Networks:
--------------------------
* Number of nodes in the network
* Number of edges in the network
* Nodes in largest WCC
* Edges in largest WCC	
* Nodes in largest SCC	
* Edges in largest SCC	
* Average clustering coefficient	
* Number of triangles of connected nodes (considering the network as undirected)
* Fraction of closed triangles (number of connected triples of nodes / number of (undirected) length 2 paths)
* Diameter (longest shortest path, maximum undirected shortest path length sampled over 1,000 random nodes)
* 90-percentile effective diameter (90-th percentile of undirected shortest path length distribution sampled over 1,000 random nodes)

Networks:
---------
* Social networks: online social networks, edges represent interactions between people
* Ground truth: ground-truth network communities in social and information networks 
* Communication: email communication networks with edges representing communication
* Citation: nodes represent papers, edges represent citations
* Collaboration: nodes represent scientists, edges represent collaborations (co-authoring a paper)
* Web graphs: nodes represent webpages and edges are hyperlinks
* Products: nodes represent products and edges link commonly co-purchased products
* p2p: nodes represent computers and edges communication
* Roads: nodes represent intersections and edges roads connecting the intersections
* Autonomous systems: graphs of the internet
* Signed networks: networks with positive and negative edges (friend/foe, trust/distrust)
* Location based networks: Social networks with geographic check-ins
* Wikipedia: Talk, editing and voting data from Wikipedia
* Memetracker: Memetracker phrases, links
* Online communities:  Data from online communities such as Reddit and Flickr
* Online reviews: Data from online review systems such as BeerAdvocate and Amazon


Mari Wahl @ 2014

