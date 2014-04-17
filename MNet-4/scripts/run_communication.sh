#!/bin/bash

mkdir ../output/graphs_sampled/communication
mkdir ../output/features_vector_sampled/communication

cd ../src/make_normalization/
python communication.py
cd ../calculate_features/
python communication.py
cd ../calculate_features_advanced/
python communication.py
cd ../..
