#!/bin/bash

wget http://snap.stanford.edu/data/twitter.tar.gz && tar xzvf twitter.tar.gz && rm twitter.tar.gz && mv twitter raw_data/social/
echo "Twiter!"

wget http://snap.stanford.edu/data/facebook.tar.gz && tar xzvf facebook.tar.gz && rm facebook.tar.gz && mv facebook raw_data/social/
echo "Facebook!"

wget http://snap.stanford.edu/data/gplus.tar.gz && tar xzvf gplus.tar.gz && rm gplus.tar.gz && mv gplus raw_data/social/
echo "gplus!"

mkdir ./raw_data/social/epinions/
wget http://snap.stanford.edu/data/soc-Epinions1.txt.gz && gzip -d soc-Epinions1.txt.gz && mv soc-Epinions1.txt raw_data/social/epinions/
echo "epinions!"

mkdir ./raw_data/social/livejournal/
wget http://snap.stanford.edu/data/soc-LiveJournal1.txt.gz && gzip -d soc-LiveJournal1.txt.gz && mv soc-LiveJournal1.txt raw_data/social/livejournal/
epinions

mkdir ./raw_data/social/pokec/
wget http://snap.stanford.edu/data/soc-pokec-relationships.txt.gz && gzip -d soc-pokec-relationships.txt.gz && mv soc-pokec-relationships.txt raw_data/echo "pokec!"

mkdir ./raw_data/social/slashdot08/
wget http://snap.stanford.edu/data/soc-Slashdot0811.txt.gz && gzip -d soc-Slashdot0811.txt.gz && mv soc-Slashdot0811.txt raw_data/social/slashdot08/
echo "slashdot1!"

mkdir ./raw_data/social/slashdot09/
wget http://snap.stanford.edu/data/soc-Slashdot0902.txt.gz && gzip -d soc-Slashdot0902.txt.gz  && mv soc-Slashdot0902.txt raw_data/social/slashdot09/
echo "slashdot2!"

mkdir ./raw_data/social/wiki/
wget http://snap.stanford.edu/data/wiki-Vote.txt.gz && gzip -d wiki-Vote.txt.gz  && mv wiki-Vote.txt raw_data/social/wiki/
echo "wiki!"


