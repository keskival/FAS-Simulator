#!/usr/bin/python -u

import numpy as np

import random
import json
import itertools

import load_data
import export_to_octave

import math
import time

[sequence, n_symbols] = load_data.load_json_data('output.json')

data = []

data_length = sequence.shape[0]
for index in range(data_length):
    print "Event: ", index+1, "/", data_length
    x = np.asfarray([[sequence[index, 0:n_symbols]]])
    data.append(np.reshape(x, n_symbols))
    export_to_octave.save('data.mat', 'data', data)
print "All done!"
