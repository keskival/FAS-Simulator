#!/bin/sh

#./run.py
#./run_easy.py
#./run_easy_with_wear_and_tear_fault.py
#./run_easy_with_retry_delay_fault.py

./utils/output_to_octave.py -i data/output.json -o data/output.mat
./utils/output_to_octave.py -i data/output_easy.json -o data/output_easy.mat
./utils/output_to_octave.py -i data/output_easy_with_wear_and_tear_fault.json -o data/output_easy_with_wear_and_tear_fault.mat
./utils/output_to_octave.py -i data/output_easy_with_retry_delay_fault.json -o data/output_easy_with_retry_delay_fault.mat

cd data
# The second argument is image width in large square pixels.
../utils/paint_sequence.m ../data/output 58
# Using the same image width here to make these comparable.
../utils/paint_sequence.m ../data/output_easy 40
../utils/paint_sequence.m ../data/output_easy_with_wear_and_tear_fault 40
../utils/paint_sequence.m ../data/output_easy_with_retry_delay_fault 40
../utils/plots.m
cd ..

cp data/*.eps data/*.tex documentation
mv data/*.eps data/*.tex documentation/YSC2017
