#!/usr/bin/python

import scipy.io as sio

import matplotlib
matplotlib.use('Agg')
import pylab

import numpy as np

import random
import json
import itertools

lastIndex = 0
symbolIndices = dict()

def get_symbol_index(symbolName):
    global lastIndex
    global symbolIndices
    if (not symbolIndices.has_key(symbolName)):
        symbolIndices[symbolName] = lastIndex
        lastIndex = lastIndex + 1
    return symbolIndices[symbolName]

def one_hot(index, size):
    vector = [0 for i in range(size)]
    vector[index] = 1
    return vector

def load_json_data(fileName):
    global lastIndex
    input = []
    lastTime = 0
    with open(fileName, 'r') as inputData:
        jsonData = json.loads(inputData.read())
        for item in jsonData:
            symbolIndex = get_symbol_index(item['type'])
        numberOfSymbols = lastIndex
    with open(fileName, 'r') as inputData:
        print("Number of symbols: ", numberOfSymbols)
        jsonData = json.loads(inputData.read())
        for item in jsonData:
            timestamp = item['timestamp']
            symbolIndex = get_symbol_index(item['type'])
            deltaTime = (timestamp - lastTime) / 1000
            lastTime = timestamp
            inputVector = one_hot(symbolIndex, numberOfSymbols) + [ deltaTime ]
            input.append(inputVector)
    return (np.asfarray(input), lastIndex)
