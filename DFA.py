#!/usr/bin/python

# This utility reads the given file and generates a DFA graph of all the possible state transitions.
# This interprets the signals as states.
import json
from pprint import pprint
from samba.dcerpc.dfs import DFS_GLOBAL_HIGH_PRIORITY_CLASS

outputJsonFile = open('output.json', 'r')
outputJson = json.load(outputJsonFile)
outputJsonFile.close()

lastItem = None
transitions = dict()
for item in outputJson:
    if (lastItem):
        # A transition from lastItem to item.type
        if (not transitions.has_key(lastItem)):
            transitions[lastItem] = dict()
        transitions[lastItem][item['type']] = 1
    lastItem = item['type']

f = open('dfa.dot', 'w')
f.write("digraph G {\n")
for fromItem in transitions.keys():
    for toItem in transitions[fromItem].keys():
        f.write("  \"" + fromItem + "\"->\"" + toItem + "\";\n")

f.write("}\n")
f.close()

