#!/bin/bash

mkdir ../output/graphs_sampled/atlas
mkdir ../output/features_vector_sampled/atlas

cd ../src/make_normalization/
python atlas.py
cd ../calculate_features/
python atlas.py
cd ../calculate_features_advanced/
python atlas.py
cd ../..
