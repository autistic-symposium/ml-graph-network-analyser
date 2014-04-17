#!/bin/bash

mkdir ../output/graphs_sampled/ground
mkdir ../output/features_vector_sampled/ground

cd ../src/make_normalization/
python ground.py
cd ../calculate_features/
python ground.py
cd ../calculate_features_advanced/
python ground.py
cd ../..
