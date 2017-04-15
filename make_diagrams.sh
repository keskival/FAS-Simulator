#!/bin/sh

./run.py
./run_easy.py
./run_easy_with_wear_and_tear_fault.py

./utils/output_to_octave.py -i data/output.json -o data/output.mat
./utils/output_to_octave.py -i data/output_easy.json -o data/output_easy.mat
./utils/output_to_octave.py -i data/output_easy_with_wear_and_tear_fault.json -o data/output_easy_with_wear_and_tear_fault.mat

./utils/paint_sequence.m data/output 58
# Using the same image width here to make these two comparable.
./utils/paint_sequence.m data/output_easy 38
./utils/paint_sequence.m data/output_easy_with_wear_and_tear_fault 38

mv data/*.eps documentation
