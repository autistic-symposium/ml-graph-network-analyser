#!/bin/bash

mkdir raw_data/
wget http://snap.stanford.edu/data/twitter.tar.gz && tar xzvf twitter.tar.gz && rm twitter.tar.gz && mv twitter raw_data/
