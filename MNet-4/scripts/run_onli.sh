#!/bin/bash

mkdir ../output/graphs_sampled/onlinecom
mkdir ../output/features_vector_sampled/onlinecom

cd ../src/make_normalization/
python onlinecom.py
cd ../calculate_features/
python onlinecom.py
cd ../calculate_features_advanced/
python onlinecom.py
cd ../..
