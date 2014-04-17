#!/bin/bash

mkdir ../output/graphs_sampled/metabolic
mkdir ../output/features_vector_sampled/metabolic

cd ../src/make_normalization/
python metabolic.py
cd ../calculate_features/
python metabolic.py
cd ../calculate_features_advanced/
python metabolic.py
cd ../..
