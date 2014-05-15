#!/bin/bash

mkdir ./raw_data/ground/livejournal_g/
wget http://snap.stanford.edu/data/bigdata/communities/com-lj.ungraph.txt.gz && gzip -d com-lj.ungraph.txt.gz && mv com-lj.ungraph.txt raw_data/ground/livejournal_g/
echo "livejournal_g!"

mkdir ./raw_data/ground/friendster/
wget http://snap.stanford.edu/data/bigdata/communities/com-friendster.ungraph.txt.gz && gzip -d com-friendster.ungraph.txt.gz && mv com-friendster.ungraph.txt raw_data/ground/friendster/
echo "friendster!"


mkdir ./raw_data/ground/orkut/
wget http://snap.stanford.edu/data/bigdata/communities/com-orkut.ungraph.txt.gz && gzip -d com-orkut.ungraph.txt.gz && mv com-orkut.ungraph.txt raw_data/ground/orkut/
echo "orkut!"

mkdir ./raw_data/ground/youtube/
wget http://snap.stanford.edu/data/bigdata/communities/com-youtube.ungraph.txt.gz && gzip -d com-youtube.ungraph.txt.gz && mv com-youtube.ungraph.txt raw_data/ground/youtube/
echo "youtube!"

mkdir ./raw_data/ground/dblp/
wget http://snap.stanford.edu/data/bigdata/communities/com-dblp.ungraph.txt.gz && gzip -d com-dblp.ungraph.txt.gz && mv com-dblp.ungraph.txt raw_data/ground/dblp/
echo "dblp!"

mkdir ./raw_data/ground/amazon/
wget http://snap.stanford.edu/data/bigdata/communities/com-amazon.ungraph.txt.gz && gzip -d com-amazon.ungraph.txt.gz && mv com-amazon.ungraph.txt raw_data/ground/amazon/
echo "amazon!"

