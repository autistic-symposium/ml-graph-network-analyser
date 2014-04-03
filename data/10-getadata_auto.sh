#!/bin/bash

mkdir ./raw_data/auto/as1/
wget http://snap.stanford.edu/data/as20000102.txt.gz && gzip -d as20000102.txt.gz && mv as20000102.txt raw_data/auto/as1/
echo "as1!"

mkdir ./raw_data/auto/as2/
wget http://snap.stanford.edu/data/as-skitter.txt.gz && gzip -d as-skitter.txt.gz && mv as-skitter.txt raw_data/auto/as2/
echo "as2!"

mkdir ./raw_data/auto/as3/
wget http://snap.stanford.edu/data/as-caida.tar.gz && tar xzvf as-caida.tar.gz && rm as-caida.tar.gz && mv as-caida* raw_data/auto/as3/
echo "as3!"

mkdir ./raw_data/auto/ore1/
wget http://snap.stanford.edu/data/oregon1_010331.txt.gz && gzip -d oregon1_010331.txt.gz && mv oregon1_010331.txt raw_data/auto/ore1/
echo "ore1-1!"

wget http://snap.stanford.edu/data/oregon1_010407.txt.gz && gzip -d oregon1_010407.txt.gz && mv oregon1_010407.txt raw_data/auto/ore1/
echo "ore1-2!"

wget http://snap.stanford.edu/data/oregon1_010414.txt.gz && gzip -d oregon1_010414.txt.gz && mv oregon1_010414.txt raw_data/auto/ore1/
echo "ore1-3!"

wget http://snap.stanford.edu/data/oregon1_010421.txt.gz && gzip -d oregon1_010421.txt.gz && mv oregon1_010421.txt raw_data/auto/ore1/
echo "ore1-4!"

wget http://snap.stanford.edu/data/oregon1_010428.txt.gz && gzip -d oregon1_010428.txt.gz && mv oregon1_010428.txt raw_data/auto/ore1/
echo "ore1-5!"

wget http://snap.stanford.edu/data/oregon1_010505.txt.gz && gzip -d oregon1_010505.txt.gz && mv oregon1_010505.txt raw_data/auto/ore1/
echo "ore1-6!"

wget http://snap.stanford.edu/data/oregon1_010512.txt.gz && gzip -d oregon1_010512.txt.gz && mv oregon1_010512.txt raw_data/auto/ore1/
echo "ore1-7!"

wget http://snap.stanford.edu/data/oregon1_010519.txt.gz && gzip -d oregon1_010519.txt.gz && mv oregon1_010519.txt raw_data/auto/ore1/
echo "ore1-8!"

wget http://snap.stanford.edu/data/oregon1_010526.txt.gz && gzip -d oregon1_010526.txt.gz && mv oregon1_010526.txt raw_data/auto/ore1/
echo "ore1-9!"

mkdir ./raw_data/auto/ore2/
wget http://snap.stanford.edu/data/oregon2_010331.txt.gz && gzip -d oregon2_010331.txt.gz && mv oregon2_010331.txt raw_data/auto/ore2/
echo "ore2-1!"

wget http://snap.stanford.edu/data/oregon2_010407.txt.gz && gzip -d oregon2_010407.txt.gz && mv oregon2_010407.txt raw_data/auto/ore2/
echo "ore2-2!"

wget http://snap.stanford.edu/data/oregon2_010414.txt.gz && gzip -d oregon2_010414.txt.gz && mv oregon2_010414.txt raw_data/auto/ore2/
echo "ore2-3!"

wget http://snap.stanford.edu/data/oregon2_010421.txt.gz && gzip -d oregon2_010421.txt.gz && mv oregon2_010421.txt raw_data/auto/ore2/
echo "ore2-4!"

wget http://snap.stanford.edu/data/oregon2_010428.txt.gz && gzip -d oregon2_010428.txt.gz && mv oregon2_010428.txt raw_data/auto/ore2/
echo "ore2-5!"

wget http://snap.stanford.edu/data/oregon2_010505.txt.gz && gzip -d oregon2_010505.txt.gz && mv oregon2_010505.txt raw_data/auto/ore2/
echo "ore2-6!"

wget http://snap.stanford.edu/data/oregon2_010512.txt.gz && gzip -d oregon2_010512.txt.gz && mv oregon2_010512.txt raw_data/auto/ore2/
echo "ore2-7!"

wget http://snap.stanford.edu/data/oregon2_010519.txt.gz && gzip -d oregon2_010519.txt.gz && mv oregon2_010519.txt raw_data/auto/ore2/
echo "ore2-8!"

wget http://snap.stanford.edu/data/oregon2_010526.txt.gz && gzip -d oregon2_010526.txt.gz && mv oregon2_010526.txt raw_data/auto/ore2/
echo "ore2-9!"


