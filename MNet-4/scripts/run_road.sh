#!/bin/bash

mkdir ../output/graphs_sampled/road
mkdir ../output/features_vector_sampled/road

cd ../src/make_normalization/
python road.py
cd ../calculate_features/
python road.py
cd ../calculate_features_advanced/
python road.py
cd ../..
