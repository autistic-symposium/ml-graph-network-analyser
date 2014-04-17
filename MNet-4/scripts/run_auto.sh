#!/bin/bash

mkdir ../output/graphs_sampled/
mkdir ../output/features_vector_sampled/
mkdir ../output/graphs_sampled/auto
mkdir ../output/features_vector_sampled/auto


cd ../src/make_normalization/
python auto.py
cd ../calculate_features/
python auto.py
cd ../calculate_features_advanced/
python auto.py
cd ../..

