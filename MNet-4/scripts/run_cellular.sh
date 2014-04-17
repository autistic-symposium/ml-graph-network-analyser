#!/bin/bash

mkdir ../output/graphs_sampled/cellular
mkdir ../output/features_vector_sampled/cellular

cd ../src/make_normalization/
python cellular.py
cd ../calculate_features/
python cellular.py
cd ../calculate_features_advanced/
python cellular.py
cd ../..
