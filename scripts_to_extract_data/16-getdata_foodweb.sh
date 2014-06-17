#!/bin/bash

mkdir ./raw_data/bio/foodweb/
wget http://vlado.fmf.uni-lj.si/pub/networks/data/bio/FoodWeb/Webs_paj.zip && gzip -d Webs_paj.zip && mv Webs_paj.* raw_data/bio/foodweb/
wget http://vlado.fmf.uni-lj.si/pub/networks/data/bio/FoodWeb/ATLSS_paj.zip && gzip -d ATLSS_paj.zip && mv ATLSS_paj.* raw_data/bio/foodweb/
echo "FoodWeb!"


