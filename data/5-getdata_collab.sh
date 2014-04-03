#!/bin/bash

mkdir ./raw_data/collaboration/astroph/
wget http://snap.stanford.edu/data/ca-AstroPh.txt.gz && gzip -d ca-AstroPh.txt.gz && mv ca-AstroPh.txt raw_data/collaboration/astroph/
echo "astroph!"

mkdir ./raw_data/collaboration/condmat/
wget http://snap.stanford.edu/data/ca-CondMat.txt.gz && gzip -d ca-CondMat.txt.gz && mv ca-CondMat.txt raw_data/collaboration/condmat/
echo "condmat!"

mkdir ./raw_data/collaboration/grqc/
wget http://snap.stanford.edu/data/ca-GrQc.txt.gz && gzip -d ca-GrQc.txt.gz && mv ca-GrQc.txt raw_data/collaboration/grqc/
echo "grqc!"

mkdir ./raw_data/collaboration/hepph/
wget http://snap.stanford.edu/data/ca-HepPh.txt.gz && gzip -d ca-HepPh.txt.gz && mv ca-HepPh.txt raw_data/collaboration/hepph/
echo "hepph!"

mkdir ./raw_data/collaboration/hepth/
wget http://snap.stanford.edu/data/ca-HepTh.txt.gz && gzip -d ca-HepTh.txt.gz && mv ca-HepTh.txt raw_data/collaboration/hepth/
echo "hepth!"



