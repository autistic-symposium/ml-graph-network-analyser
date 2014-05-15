#!/bin/bash

mkdir ./raw_data/location/gowalla/
wget http://snap.stanford.edu/data/loc-gowalla_edges.txt.gz && gzip -d loc-gowalla_edges.txt.gz && mv loc-gowalla_edges.txt raw_data/location/gowalla/
echo "gowalla!"

mkdir ./raw_data/location/bright/
wget http://snap.stanford.edu/data/loc-brightkite_edges.txt.gz && gzip -d loc-brightkite_edges.txt.gz && mv loc-brightkite_edges.txt raw_data/location/bright/
echo "bright!"


