'''
Run the snowball sampling.

mari wahl @ 2014
'''


from helpers import constants, running

PATH_2_OUTPUT = constants.PATH_2_GRAPH_SAMPLED
PATH_2_INPUT = constants.PATH_2_GRAPH_GLOBAL

NUM_SAMPLES = constants.NUMBER_OF_RANDOM_SAMPLES 
DEPTH = constants.DEPTH_SAMPLE

# change here for type of net:
NETWORK_FILES_UN  = constants.NETWORK_FILES_UN_SOCIAL 
NETWORK_FILES_DIR = constants.NETWORK_FILES_DIR_SOCIAL 

TYPE_NET_DIR = "social/"

NUMBER_OF_NETWORKS_DIR = [ 973, 132]
NUMBER_OF_NETWORKS_UN = [10]



def main():

    running.sampling_tar_dir(NETWORK_FILES_DIR, NUMBER_OF_NETWORKS_DIR, PATH_2_INPUT, TYPE_NET_DIR, NUM_SAMPLES, PATH_2_OUTPUT,DEPTH)

    running.sampling_tar_un(NETWORK_FILES_UN, NUMBER_OF_NETWORKS_UN, PATH_2_INPUT, TYPE_NET_DIR, NUM_SAMPLES, PATH_2_OUTPUT,DEPTH)

    print("All graphs for " + TYPE_NET_DIR + " were processed. The end! \n")
 

if __name__ == '__main__':
    main()


        
