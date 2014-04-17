#!/bin/bash

mkdir ../output/graphs_sampled/wiki
mkdir ../output/features_vector_sampled/wiki

cd ../src/make_normalization/
python wiki.py
cd ../calculate_features/
python wiki.py
cd ../calculate_features_advanced/
python wiki.py
cd ../..
