#!/bin/bash


wget http://snap.stanford.edu/data/facebook.tar.gz && tar xzvf facebook.tar.gz && rm facebook.tar.gz && mv facebook raw_data/
wget http://snap.stanford.edu/data/gplus.tar.gz && tar xzvf gplus.tar.gz && rm gplus.tar.gz && mv gplus raw/

mkdir arxiv
wget http://snap.stanford.edu/data/ca-AstroPh.txt.gz && tar xzvf ca-AstroPh.txt.gz && rm ca-AstroPh.txt.gz && mv ca-AstroPh.txt raw/arxiv/ 

