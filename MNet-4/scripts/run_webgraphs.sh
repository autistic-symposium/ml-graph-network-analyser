#!/bin/bash

mkdir ../output/graphs_sampled/webgraphs
mkdir ../output/features_vector_sampled/webgraphs

cd ../src/make_normalization/
python webgraphs.py
cd ../calculate_features/
python webgraphs.py
cd ../calculate_features_advanced/
python webgraphs.py
cd ../..
