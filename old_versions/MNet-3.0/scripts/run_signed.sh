#!/bin/bash

mkdir ../output/graphs_sampled/signed
mkdir ../output/features_vector_sampled/signed

cd ../src/make_normalization/
python signed.py
cd ../calculate_features/
python signed.py
cd ../calculate_features_advanced/
python signed.py
cd ../..
