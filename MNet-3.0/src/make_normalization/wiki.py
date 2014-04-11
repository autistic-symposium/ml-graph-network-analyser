'''
Run the snowball sampling.

mari wahl @ 2014
'''

from helpers import constants, running

NUM_SAMPLES = constants.NUMBER_OF_RANDOM_SAMPLES 
DEPTH = constants.DEPTH_SAMPLE

PATH_2_OUTPUT = constants.PATH_2_GRAPH_SAMPLED
PATH_2_INPUT = constants.PATH_2_GRAPH_GLOBAL



# change here for type of net:
NETWORK_FILES = constants.NETWORK_FILES_DIR_WIKI
TYPE_NET_DIR = "wiki/"



def main():


    running.sampling_dir(NETWORK_FILES, PATH_2_INPUT, TYPE_NET_DIR, NUM_SAMPLES, PATH_2_OUTPUT, DEPTH)
    print("All graphs for " + TYPE_NET_DIR + " were processed. The end! \n")
 
   


if __name__ == '__main__':
    main()
