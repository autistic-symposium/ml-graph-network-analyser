#!/bin/bash

mkdir ./raw_data/meme/sn/
wget http://snap.stanford.edu/data/higgs-social_network.edgelist.gz && gzip -d higgs-social_network.edgelist.gz && mv higgs-social_network.edgelist raw_data/meme/sn/
echo "sn!"

mkdir ./raw_data/meme/retweet/
wget http://snap.stanford.edu/data/higgs-retweet_network.edgelist.gz && gzip -d higgs-retweet_network.edgelist.gz && mv higgs-retweet_network.edgelist raw_data/meme/retweet/
echo "retweet!"

mkdir ./raw_data/meme/reply/
wget http://snap.stanford.edu/data/higgs-reply_network.edgelist.gz && gzip -d higgs-reply_network.edgelist.gz && mv higgs-reply_network.edgelist raw_data/meme/reply/
echo "reply!"

mkdir ./raw_data/meme/mention/
wget http://snap.stanford.edu/data/higgs-mention_network.edgelist.gz && gzip -d higgs-mention_network.edgelist.gz && mv higgs-mention_network.edgelist raw_data/meme/mention/
echo "mention!"


