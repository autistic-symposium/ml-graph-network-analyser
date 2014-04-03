#!/bin/bash

mkdir ./raw_data/communication/euall/
wget http://snap.stanford.edu/data/email-EuAll.txt.gz && gzip -d email-EuAll.txt.gz && mv email-EuAll.txt raw_data/communication/euall/
echo "euall!"

mkdir ./raw_data/communication/enron/
wget http://snap.stanford.edu/data/email-Enron.txt.gz && gzip -d email-Enron.txt.gz && mv email-Enron.txt raw_data/communication/enron/
echo "enron!"

mkdir ./raw_data/communication/wiki-talk/
wget http://snap.stanford.edu/data/wiki-Talk.txt.gz && gzip -d wiki-Talk.txt.gz && mv wiki-Talk.txt raw_data/communication/wiki-talk/
echo "wiki-talk!"


