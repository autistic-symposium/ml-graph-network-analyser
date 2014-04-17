#!/bin/bash

mkdir ../output/graphs_sampled/social
mkdir ../output/features_vector_sampled/social

cd ../src/make_normalization/
python social_I.py
cd ../calculate_features/
python social_I.py
cd ../calculate_features_advanced/
python social_I.py
cd ../..
