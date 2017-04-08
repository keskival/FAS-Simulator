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

# Moore reduction here
itemToKPartition = dict()
kPartitionToItems = dict()

f = open('dfa.dot', 'w')
f.write("digraph G {\n")
for fromItem in transitions.keys():
    # We will try to do minimization here also.
    toItems = transitions[fromItem].keys()
    for toItem in toItems:
        f.write("  \"" + fromItem + "\"->\"" + toItem + "\";\n")
    k = ":".join(sorted(toItems))
    # All fromItems in the same kPartition are kEquivalent, because their outputs are the same.
    itemToKPartition[fromItem] = k
    if (not kPartitionToItems.has_key(k)):
        kPartitionToItems[k] = []
    kPartitionToItems[k].append(fromItem)
print kPartitionToItems
f.write("}\n")
f.close()

f_reduced = open('dfa_reduced.dot', 'w')
f_reduced.write("digraph G {\n")

transitions_reduced = dict()

# Reducing. One iteration is enough.
for fromItemRaw in transitions.keys():
    fromItemK = itemToKPartition[fromItemRaw]
    fromItem = ":".join(sorted(kPartitionToItems[fromItemK]))
    print fromItem

    toItemsRaw = transitions[fromItemRaw].keys()
    toItems = dict()
    for toItemRaw in toItemsRaw:
        toItemK = itemToKPartition[toItemRaw]
        toItemKey = ":".join(sorted(kPartitionToItems[toItemK]))
        toItems[toItemKey] = 1
    transitions_reduced[fromItem] = toItems.keys()

for fromItem in transitions_reduced.keys():
    # We will try to do minimization here also.
    toItems = transitions_reduced[fromItem]
    for toItem in toItems:
        f_reduced.write("  \"" + fromItem + "\"->\"" + toItem + "\";\n")
f_reduced.write("}\n")
f_reduced.close()
