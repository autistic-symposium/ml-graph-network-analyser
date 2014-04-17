#!/bin/bash

mkdir ../output/graphs_sampled/p2p
mkdir ../output/features_vector_sampled/p2p

cd ../src/make_normalization/
python p2p.py
cd ../calculate_features/
python p2p.py
cd ../calculate_features_advanced/
python p2p.py
cd ../..
