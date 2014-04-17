#!/bin/bash

mkdir ../output/graphs_sampled/meme
mkdir ../output/features_vector_sampled/meme

cd ../src/make_normalization/
python meme.py
cd ../src/calculate_features/
python meme.py
cd ../calculate_features_advanced/
python meme.py
cd ../..
