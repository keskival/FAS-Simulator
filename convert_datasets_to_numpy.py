#!/usr/bin/python3

import simpy
import os
import json
import numpy as np

from modules.process.production_line import ProductionLine
from modules.components.clock import Clock

NUMBER_OF_RUNS = 100000

os.makedirs("numpy_data/runs_with_errors", exist_ok=True)
os.makedirs("numpy_data/correct_runs", exist_ok=True)

# Getting all event types to make an index out of them.
production_line = ProductionLine(None, None, False)
clock = Clock(None, None, False)
all_event_types = clock.get_events() + production_line.get_events()
event_id_for_type = dict()
for event_index, event_type in enumerate(all_event_types):
    event_id_for_type[event_type] = event_index

max_length_correct = 0
min_length_correct = None
for run in range(NUMBER_OF_RUNS):
    print(f"Converting correct run {run}/{NUMBER_OF_RUNS}")
    filename = f"data/correct_runs/{run}.json"
    numpy_filename = f"numpy_data/correct_runs/{run}.npy"
    with open(filename, "r") as json_run_file:
        events = json.load(json_run_file)
        run = []
        for event in events:
            timestamp = event["timestamp"]
            event_type = event["type"]
            event_id = event_id_for_type[event_type]
            # We will only store events in sequence.
            run.append(np.array(event_id))
        numpy_run = np.stack(run)
        if len(run) > max_length_correct:
            max_length_correct = len(run)
        if min_length_correct is None or len(run) < min_length_correct:
            min_length_correct = len(run)

        np.save(numpy_filename, numpy_run)

max_length_faulty = 0
min_length_faulty = None
for run in range(NUMBER_OF_RUNS):
    print(f"Converting faulty run {run}/{NUMBER_OF_RUNS}")
    filename = f"data/runs_with_errors/{run}.json"
    numpy_filename = f"numpy_data/runs_with_errors/{run}.npy"
    with open(filename, "r") as json_run_file:
        events = json.load(json_run_file)
        run = []
        for event in events:
            timestamp = event["timestamp"]
            event_type = event["type"]
            event_id = event_id_for_type[event_type]
            # We will only store events in sequence.
            run.append(np.array(event_id))
        numpy_run = np.stack(run)
        if len(run) > max_length_faulty:
            max_length_faulty = len(run)
        if min_length_faulty is None or len(run) < min_length_faulty:
            min_length_faulty = len(run)

        np.save(numpy_filename, numpy_run)

print(f"Correct runs: Max run length: {max_length_correct}, Min run length: {min_length_correct}")
print(f"Runs with errors: Max run length: {max_length_faulty}, Min run length: {min_length_faulty}")
print("Done.")
