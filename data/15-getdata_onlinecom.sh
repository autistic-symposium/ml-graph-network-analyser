#!/bin/bash

mkdir ./raw_data/onlinecom/reddit/
wget http://snap.stanford.edu/data/redditSubmissions.csv.gz && gzip -d redditSubmissions.csv.gz && mv redditSubmissions.csv raw_data/onlinecom/reddit/
echo "reddit!"

mkdir ./raw_data/onlinecom/flickr/
wget http://snap.stanford.edu/data/flickrEdges.txt.gz && gzip -d flickrEdges.txt.gz && mv flickrEdges.txt raw_data/onlinecom/flickr/
echo "flickr!"


