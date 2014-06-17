#!/bin/bash

mkdir ./raw_data/bio/yeast/
wget http://vlado.fmf.uni-lj.si/pub/networks/data/bio/Yeast/yeast.zip && gzip -d yeast.zip && mv yeast.zip.* raw_data/bio/yeast/
echo "yeast!"


