#!/bin/bash

mkdir ./raw_data/wiki/vote/
wget http://snap.stanford.edu/data/wiki-Vote.txt.gz && gzip -d wiki-Vote.txt.gz && mv wiki-Vote.txt raw_data/wiki/vote/
echo "vote!"

mkdir ./raw_data/wiki/talk/
wget http://snap.stanford.edu/data/wiki-Talk.txt.gz && gzip -d wiki-Talk.txt.gz && mv wiki-Talk.txt raw_data/wiki/talk/
echo "talk!"

mkdir ./raw_data/wiki/elec/
wget http://snap.stanford.edu/data/wikiElec.ElecBs3.txt.gz && gzip -d wikiElec.ElecBs3.txt.gz && mv wikiElec.ElecBs3.txt raw_data/wiki/elec/
echo "elec!"



