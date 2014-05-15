#!/bin/bash

mkdir ./raw_data/products/amazon1/
wget http://snap.stanford.edu/data/amazon0302.txt.gz && gzip -d amazon0302.txt.gz && mv amazon0302.txt raw_data/products/amazon1/
echo "amazon1!"

mkdir ./raw_data/products/amazon2/
wget http://snap.stanford.edu/data/amazon0312.txt.gz && gzip -d amazon0312.txt.gz && mv amazon0312.txt raw_data/products/amazon2/
echo "amazon2!"

mkdir ./raw_data/products/amazon3/
wget http://snap.stanford.edu/data/amazon0505.txt.gz && gzip -d amazon0505.txt.gz && mv amazon0505.txt raw_data/products/amazon3/
echo "amazon3!"

mkdir ./raw_data/products/amazon4/
wget http://snap.stanford.edu/data/amazon0601.txt.gz && gzip -d amazon0601.txt.gz && mv amazon0601.txt raw_data/products/amazon4/
echo "amazon4!"

mkdir ./raw_data/products/amazonmeta/
wget http://snap.stanford.edu/data/bigdata/amazon/amazon-meta.txt.gz && gzip -d amazon-meta.txt.gz && mv amazon-meta.txt raw_data/products/amazonmeta/
echo "amazonmeta!"



