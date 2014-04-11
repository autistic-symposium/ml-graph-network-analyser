#!/bin/bash

mkdir ../output/graphs_sampled/citation
mkdir ../output/features_vector_sampled/citation

cd ../src/make_normalization/
python citation.py
cd ../calculate_features/
python citation.py
cd ../calculate_features_advanced/
python citation.py
cd ../..
