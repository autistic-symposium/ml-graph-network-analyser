#!/bin/bash

mkdir ./raw_data/road/ca/
wget http://snap.stanford.edu/data/roadNet-CA.txt.gz && gzip -d roadNet-CA.txt.gz && mv roadNet-CA.txt raw_data/road/ca/
echo "ca!"

mkdir ./raw_data/road/pa/
wget http://snap.stanford.edu/data/roadNet-PA.txt.gz && gzip -d roadNet-PA.txt.gz && mv roadNet-PA.txt raw_data/road/pa/
echo "pa!"

mkdir ./raw_data/road/tx/
wget http://snap.stanford.edu/data/roadNet-TX.txt.gz && gzip -d roadNet-TX.txt.gz && mv roadNet-TX.txt raw_data/road/tx/
echo "tx!"



