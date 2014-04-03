'''
This script make the correlation plots for each feature and each network.
The correlation plots show how a feature change with the size of the network and
it is useful to decide about the normalization.

mari wahl @ 2014
'''

import pylab
import os
pylab.rcParams.update({'font.size': 4})
FEATURE_NAMES = [ 'Assortivity', 'Mean Betweness Centrality', 'Mean Clique Number',  'Average Clustering Coefficient',  'Egde Connectivity', 'Vertex Connectivity', 'Coreness', 'Diameter', 'Distortion', 'Eccentricity', 'Expansion', 'Girth', 'Hop Count']
    


def plot_features(NETWORK_VECTOR_FILES, PATH_TO_INPUT, PATH_TO_OUTPUT):

    for network_raw_type in NETWORK_VECTOR_FILES:

        datalist = pylab.loadtxt(PATH_TO_INPUT + network_raw_type + '.dat', unpack=True) 
        f, ax = pylab.subplots(4, 4)
        f.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.4, hspace=0.05)

    	for i, name in enumerate(FEATURE_NAMES):           
            if i < 4:
                ax[0, i].plot(datalist[0], datalist[i+1], 'g.')	
                ax[0, i].set_ylabel(name, fontsize=6)       
            elif i >=4 and i <8:
                ax[1, i-4].plot(datalist[0], datalist[i+1], 'g.')	
                ax[1, i-4].set_ylabel(name, fontsize=6)     
	    elif i >=8 and i <12:
                ax[2, i-8].plot(datalist[0], datalist[i+1], 'g.', label='test')	
                ax[2, i-8].set_ylabel(name, fontsize=6)     
            else:
                ax[3, i-12].plot(datalist[0], datalist[i+1], 'g.')	
                ax[3, i-12].set_ylabel(name, fontsize=6)     

    	pylab.savefig(PATH_TO_OUTPUT + network_raw_type + '.png')






def main():
    # 1-social, 2-ground-truth, 3-communication, 4-citation, 5-collaboration, 6-web graphs
    # 7-products, 8-p2p, 9-road, 10-autonomous systems, 11-signed networks, 12-location-based
    # networks, 13-wikipedia, 14-memetracker, 15-online communities, 16-online reviews
    NETWORK_TYPE = 1 

    if NETWORK_TYPE == 1: # social
	    PATH_TO_INPUT = "../features_vector/social/" 
	    PATH_TO_OUTPUT = "../plots/social/"
	    NETWORK_VECTOR_FILES = ["twitter", "facebook", "gplus", "epinions", "livejournal", "pokec", "slashdot08", "slashdot09", "wiki" ]

    if NETWORK_TYPE == 2: # groud-trhuth communities
	    PATH_TO_INPUT = "../features_vector/ground/" 
	    PATH_TO_OUTPUT = "../plots/ground/"
	    NETWORK_VECTOR_FILES = ["livejournal_g", "friendster", "orkut", "youtube", "dblp", "amazon" ]	 

    if NETWORK_TYPE == 3: # communication
	    PATH_TO_INPUT = "../features_vector/communication/" 
	    PATH_TO_OUTPUT = "../plots/communication/"
	    NETWORK_VECTOR_FILES = ["euall", "enron", "wiki-talk"]

    if NETWORK_TYPE == 4: # citation
	    PATH_TO_INPUT = "../features_vector/citation/" 
	    PATH_TO_OUTPUT = "../plots/citation/"
	    NETWORK_VECTOR_FILES = ["hepph", "hepth", "patents"]


    if NETWORK_TYPE == 5: # collaboration
	    PATH_TO_INPUT = "../features_vector/collaboration/" 
	    PATH_TO_OUTPUT = "../plots/collaboration/"
	    NETWORK_VECTOR_FILES = ["astroph", "condmat", "grqc", "hepph", "hepth"]

    if NETWORK_TYPE == 6: # web graphs
	    PATH_TO_INPUT = "../features_vector/webgraphs/" 
	    PATH_TO_OUTPUT = "../plots/webgraphs/"
	    NETWORK_VECTOR_FILES = ["berkstan", "google", "notredame", "stanford"]

    if NETWORK_TYPE == 7: # product purchasing
	    PATH_TO_INPUT = "../features_vector/products/" 
	    PATH_TO_OUTPUT = "../plots/products/"
	    NETWORK_VECTOR_FILES = ["amazon1", "amazon2", "amazon3", "amazon4", "amazonmeta"]

    if NETWORK_TYPE == 8: # p2p
	    PATH_TO_INPUT = "../features_vector/p2p/" 
	    PATH_TO_OUTPUT = "../plots/p2p/"
	    NETWORK_VECTOR_FILES = ["gnutella1", "gnutella2", "gnutella3", "gnutella4", "gnutella5", "gnutella6", "gnutella7", "gnutella8", "gnutella9"]

    if NETWORK_TYPE == 9: # road
	    PATH_TO_INPUT = "../features_vector/road/" 
	    PATH_TO_OUTPUT = "../plots/road/"
	    NETWORK_VECTOR_FILES = ["ca", "pa", "tx"]

    if NETWORK_TYPE == 10: # autonomous systems graphs
	    PATH_TO_INPUT = "../features_vector/auto/" 
	    PATH_TO_OUTPUT = "../plots/auto/"
	    NETWORK_VECTOR_FILES = ["as1", "as2", "as3", "ore1", "ore2"]

    if NETWORK_TYPE == 11: # signed networks
	    PATH_TO_INPUT = "../features_vector/signed/" 
	    PATH_TO_OUTPUT = "../plots/signed/"
	    NETWORK_VECTOR_FILES = ["soc1", "soc2", "soc3", "soc4", "wiki-ele"]

    if NETWORK_TYPE == 11: # signed networks
	    PATH_TO_INPUT = "../features_vector/signed/" 
	    PATH_TO_OUTPUT = "../plots/signed/"
	    NETWORK_VECTOR_FILES = ["soc1", "soc2", "soc3", "soc4", "wiki-ele"]

    if NETWORK_TYPE == 12: # location-based online social networks
	    PATH_TO_INPUT = "../features_vector/location/" 
	    PATH_TO_OUTPUT = "../plots/location/"
	    NETWORK_VECTOR_FILES = ["gowalla", "bright"]

    if NETWORK_TYPE == 13: #  wikipedia
	    PATH_TO_INPUT = "../features_vector/wiki/" 
	    PATH_TO_OUTPUT = "../plots/wiki/"
	    NETWORK_VECTOR_FILES = ["vote", "talk", "elec", "meta"]

    if NETWORK_TYPE == 14: # memetracker
	    PATH_TO_INPUT = "../features_vector/meme/" 
	    PATH_TO_OUTPUT = "../plots/meme/"
	    NETWORK_VECTOR_FILES = ["twitter7", "meme", "ksc", "higgs"]

    if NETWORK_TYPE == 15: # online communties
	    PATH_TO_INPUT = "../features_vector/onlinecom/" 
	    PATH_TO_OUTPUT = "../plots/onlinecom/"
	    NETWORK_VECTOR_FILES = ["reddit", "flickr"]

    if NETWORK_TYPE == 16: # online reviews
	    PATH_TO_INPUT = "../features_vector/reviews/" 
	    PATH_TO_OUTPUT = "../plots/reviews/"
	    NETWORK_VECTOR_FILES = ["beer", "rate", "cellar", "amazon", "fine", "movies"]




    if not os.path.exists(PATH_TO_OUTPUT):
        os.makedirs(PATH_TO_OUTPUT)

    try:
        os.path.exists(PATH_TO_INPUT)
    except IOError:
        print("Feature vectors not found.")

    plot_features(NETWORK_VECTOR_FILES, PATH_TO_INPUT, PATH_TO_OUTPUT)
      

  


if __name__ == '__main__':
    main()

