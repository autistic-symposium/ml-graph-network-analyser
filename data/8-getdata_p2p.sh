#!/bin/bash

mkdir ./raw_data/p2p/gnutella1/
wget http://snap.stanford.edu/data/p2p-Gnutella04.txt.gz && gzip -d p2p-Gnutella04.txt.gz && mv p2p-Gnutella04.txt raw_data/p2p/gnutella1/
echo "gnutella1!"

mkdir ./raw_data/p2p/gnutella2/
wget http://snap.stanford.edu/data/p2p-Gnutella05.txt.gz && gzip -d p2p-Gnutella05.txt.gz && mv p2p-Gnutella05.txt raw_data/p2p/gnutella2/
echo "gnutella2!"

mkdir ./raw_data/p2p/gnutella3/
wget http://snap.stanford.edu/data/p2p-Gnutella06.txt.gz && gzip -d p2p-Gnutella06.txt.gz && mv p2p-Gnutella06.txt raw_data/p2p/gnutella3/
echo "gnutella3!"

mkdir ./raw_data/p2p/gnutella4/
wget http://snap.stanford.edu/data/p2p-Gnutella08.txt.gz && gzip -d p2p-Gnutella08.txt.gz && mv p2p-Gnutella08.txt raw_data/p2p/gnutella4/
echo "gnutella4!"

mkdir ./raw_data/p2p/gnutella5/
wget http://snap.stanford.edu/data/p2p-Gnutella09.txt.gz && gzip -d p2p-Gnutella09.txt.gz && mv p2p-Gnutella09.txt raw_data/p2p/gnutella5/
echo "gnutella5!"

mkdir ./raw_data/p2p/gnutella6/
wget http://snap.stanford.edu/data/p2p-Gnutella24.txt.gz && gzip -d p2p-Gnutella24.txt.gz && mv p2p-Gnutella24.txt raw_data/p2p/gnutella6/
echo "gnutella6!"

mkdir ./raw_data/p2p/gnutella7/
wget http://snap.stanford.edu/data/p2p-Gnutella25.txt.gz && gzip -d p2p-Gnutella25.txt.gz && mv p2p-Gnutella25.txt raw_data/p2p/gnutella7/
echo "gnutella7!"

mkdir ./raw_data/p2p/gnutella8/
wget http://snap.stanford.edu/data/p2p-Gnutella30.txt.gz&& gzip -d p2p-Gnutella30.txt.gz && mv p2p-Gnutella30.txt raw_data/p2p/gnutella8/
echo "gnutella8!"

mkdir ./raw_data/p2p/gnutella9/
wget http://snap.stanford.edu/data/p2p-Gnutella31.txt.gz && gzip -d p2p-Gnutella31.txt.gz && mv p2p-Gnutella31.txt raw_data/p2p/gnutella9/
echo "gnutella9!"


