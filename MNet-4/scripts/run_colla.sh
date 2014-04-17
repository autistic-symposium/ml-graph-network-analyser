#!/bin/bash

mkdir ../output/graphs_sampled/collaboration
mkdir ../output/features_vector_sampled/collaboration

cd ../src/make_normalization/
python collaboration.py
cd ../calculate_features/
python collaboration.py
cd ../calculate_features_advanced/
python collaboration.py
cd ../..
