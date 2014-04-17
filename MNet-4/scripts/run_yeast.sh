#!/bin/bash

mkdir ../output/graphs_sampled/yeast
mkdir ../output/features_vector_sampled/yeast

cd ../src/make_normalization/
python yeast.py
cd ../calculate_features/
python yeast.py
cd ../calculate_features_advanced/
python yeast.py
cd ../..
