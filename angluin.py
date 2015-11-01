#!/usr/bin/python

# This utility reads the given file, and uses an L*, that is, Angluin learner to infer the implicit DFA.
import json
import sys, os
sys.path.append("./lib/netzob/src/")
from netzob.Common.Vocabulary import Vocabulary
from netzob.Inference.Grammar.Angluin import Angluin

outputJsonFile = open('output.json', 'r')
outputJson = json.load(outputJsonFile)
outputJsonFile.close()

lastItem = None
# We will encode the event sequence into a string of one-character symbols to allow fast searching
# of matches.
sequence = ""

maxId = 0
types = dict()

def type_to_id(type):
    global maxId, types
    if (types.has_key(type)):
        return types[type]
    else:
        types[type] = maxId
        maxId = maxId + 1
        return types[type]

def id_to_char(id):
    return chr(ord('A') + id)

for item in outputJson:
    id = type_to_id(item["type"])
    sequence = sequence + id_to_char(id)

print sequence
print len(sequence)
print len(types)

vocabulary = Vocabulary()

# __init__(self, dictionary, inputDictionary, communicationChannel, resetScript, cb_query, cb_hypotheticalAutomaton, cache)
angluinLearner = Angluin()
