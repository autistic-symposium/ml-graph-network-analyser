#!/bin/bash

mkdir ../output/graphs_sampled/social
mkdir ../output/features_vector_sampled/social

#cd ../src/make_normalization/
#python social_II.py
cd ../src/calculate_features/
python social_II.py
cd ../calculate_features_advanced/
python social_II.py
cd ../..

