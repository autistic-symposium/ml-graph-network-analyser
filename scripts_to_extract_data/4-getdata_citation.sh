#!/bin/bash

mkdir ./raw_data/citation/hepph/
wget http://snap.stanford.edu/data/cit-HepPh.txt.gz && gzip -d cit-HepPh.txt.gz  && mv cit-HepPh.txt raw_data/citation/hepph/
echo "hepph!"

mkdir ./raw_data/citation/hepth/
wget http://snap.stanford.edu/data/cit-HepTh.txt.gz && gzip -d cit-HepTh.txt.gz && mv cit-HepTh.txt raw_data/citation/hepth/
echo "hepth!"

mkdir ./raw_data/citation/patents/
wget http://snap.stanford.edu/data/cit-Patents.txt.gz && gzip -d cit-Patents.txt.gz && mv cit-Patents.txt raw_data/citation/patents/
echo "patents!"


