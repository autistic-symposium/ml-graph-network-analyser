#!/bin/bash

mkdir ../output/graphs_sampled/carbon
mkdir ../output/features_vector_sampled/carbon

cd ../src/make_normalization/
python carbon.py
cd ../calculate_features/
python carbon.py
cd ../calculate_features_advanced/
python carbon.py
cd ../..
