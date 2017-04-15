#!/usr/bin/python -u

import numpy as np

import random
import json
import itertools

import load_data
import export_to_octave

import math
import time
import argparse

parser = argparse.ArgumentParser(description="Translates the JSON output to Octave mat file for graphing.")
parser.add_argument("-i", "--input", default="output.json")
parser.add_argument("-o", "--output", default="data.mat")
params = parser.parse_args()

[sequence, n_symbols] = load_data.load_json_data(params.input)

data = []

data_length = sequence.shape[0]
for index in range(data_length):
    print "Event: ", index+1, "/", data_length
    x = np.asfarray([[sequence[index, 0:n_symbols]]])
    data.append(np.reshape(x, n_symbols))
    export_to_octave.save(params.output, "data", data)
print "All done!"
