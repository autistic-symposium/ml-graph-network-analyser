#!/bin/bash

mkdir ../output/graphs_sampled/products
mkdir ../output/features_vector_sampled/products

cd ../src/make_normalization/
python products.py
cd ../calculate_features/
python products.py
cd ../calculate_features_advanced/
python products.py
cd ../..
