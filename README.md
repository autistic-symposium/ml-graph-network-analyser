## ml-graph-network-analyser

<br>

#### 👉 this project contains the source code for the extraction and analysis of several graph (complex networks) features from publicly available datasets with [NetworkX](https://networkx.org/)
#### 👉 [read the final research paper here](on-classifying-complex-networks-by-their-features.pdf)


<br>

---

### analyzed features

<br>

* assortativity
* clique number
* clustering
* density
* diameter
* edge connectivity
* node connectivity
* number of cliques
* number of edges
* number of nodes
* radius
* clustering and transitivity
* betweenness centrality
* closeness centrality
* communicability centrality
* coreness
* degree centrality
* eccentricity
* number of triangles
* pagerank
* square clustering
* transitivity

<br>

---

### analyzed networks

<br>

* **social networks**: online social networks, edges represent interactions between people
* **ground truth**: ground-truth network communities in social and information networks
* **communication**: email communication networks with edges representing communication
* **citation**: nodes represent papers, edges represent citations
* **collaboration**: nodes represent scientists, edges represent collaborations (co-authoring a paper)
* **web graphs**: nodes represent webpages and edges are hyperlinks
* **products**: nodes represent products and edges link commonly co-purchased products
* **p2p**: nodes represent computers and edges represent communication
* **roads**: nodes represent intersections and edges roads connecting the intersections
* **autonomous systems**: graphs of the internet
* **signed networks**: networks with positive and negative edges (friend/foe, trust/distrust)
* **location-based networks**: Social networks with geographic check-ins
* **wikipedia**: yalk, editing and voting data from Wikipedia
* **bio atlas**: food-webs selected from the ecosystem network analysis resources
* **bio-cellular**: substrate in the cellular network of the corresponding organism
* **bio-metabolic**: metabolic network of the corresponding organisms
* **bio-carbon**: carbon exchanges in the cypress wetlands of south florida during the wet and dry season
* **bio yeast**: protein-protein interaction network in budding yeast

<br>


---

### additional considerations

<br>

#### normalization and graph sampling

* performed using snowball sampling (choosing the sample order, i.e., number of nodes)
* optimized for the number of edges and multiple samplings

<br>

#### next steps in the data pipeline


* **[1. cleanse the data, with ml-netclean](https://github.com/autistic-symposium/ml-netclean)**
* **[2. classify the networks with several machine learning techniques, with mlnet](https://github.com/autistic-symposium/mlnet-complex-networks)**

