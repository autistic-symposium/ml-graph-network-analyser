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
NETWORK_FILES_UN = constants.NETWORK_FILES_UN_ATLAS 
TYPE_NET_DIR = "atlas/"





def main():

    running.sampling_un(NETWORK_FILES_UN, PATH_2_INPUT, TYPE_NET_DIR, NUM_SAMPLES, PATH_2_OUTPUT, DEPTH)

    print("All graphs for " + TYPE_NET_DIR + " were processed. The end! \n")
 
   


if __name__ == '__main__':
    main()
