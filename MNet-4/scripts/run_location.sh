#!/bin/bash

mkdir ../output/graphs_sampled/location
mkdir ../output/features_vector_sampled/location

cd ../src/make_normalization/
python location.py
cd ../calculate_features/
python location.py
cd ../calculate_features_advanced/
python location.py
cd ../..
