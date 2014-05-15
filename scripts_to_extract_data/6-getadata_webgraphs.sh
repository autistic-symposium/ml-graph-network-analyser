#!/bin/bash

mkdir ./raw_data/webgraphs/berkstan/
wget http://snap.stanford.edu/data/web-BerkStan.txt.gz && gzip -d web-BerkStan.txt.gz && mv web-BerkStan.txt raw_data/webgraphs/berkstan/
echo "berkstan!"

mkdir ./raw_data/webgraphs/google/
wget http://snap.stanford.edu/data/web-Google.txt.gz && gzip -d web-Google.txt.gz && mv web-Google.txt raw_data/webgraphs/google/
echo "google!"

mkdir ./raw_data/webgraphs/notredame/
wget http://snap.stanford.edu/data/web-NotreDame.txt.gz && gzip -d web-NotreDame.txt.gz && mv web-NotreDame.txt raw_data/webgraphs/notredame/
echo "notredame!"

mkdir ./raw_data/webgraphs/stanford/
wget http://snap.stanford.edu/data/web-Stanford.txt.gz && gzip -d web-Stanford.txt.gz && mv web-Stanford.txt raw_data/webgraphs/stanford/
echo "stanford!"

