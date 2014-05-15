#!/bin/bash

mkdir ./raw_data/signed/soc1/
wget http://snap.stanford.edu/data/soc-sign-epinions.txt.gz && gzip -d soc-sign-epinions.txt.gz && mv soc-sign-epinions.txt raw_data/signed/soc1/
echo "soc1!"

mkdir ./raw_data/signed/soc2/
wget http://snap.stanford.edu/data/soc-sign-Slashdot081106.txt.gz && gzip -d soc-sign-Slashdot081106.txt.gz && mv soc-sign-Slashdot081106.txt raw_data/signed/soc2/
echo "soc2!"

mkdir ./raw_data/signed/soc3/
wget http://snap.stanford.edu/data/soc-sign-Slashdot090216.txt.gz && gzip -d soc-sign-Slashdot090216.txt.gz && mv soc-sign-Slashdot090216.txt raw_data/signed/soc3/
echo "soc3!"

mkdir ./raw_data/signed/soc4/
wget http://snap.stanford.edu/data/soc-sign-Slashdot090221.txt.gz&& gzip -d soc-sign-Slashdot090221.txt.gz && mv soc-sign-Slashdot090221.txt raw_data/signed/soc4/
echo "soc4!"


mkdir ./raw_data/signed/wiki-ele/
wget http://snap.stanford.edu/data/wikiElec.ElecBs3.txt.gz && gzip -d wikiElec.ElecBs3.txt.gz && mv wikiElec.ElecBs3.txt raw_data/signed/wiki-ele/
echo "wiki-ele!"


