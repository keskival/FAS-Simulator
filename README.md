# FAS Simulator

A modular benchmark simulator for Flexible Assembly Systems (FAS) or Flexible Manufacturing Systems (FMS).

Licence: WTFPL

This project includes a SimPy discrete event simulator simulating a plausible Flexible Assembly System
documented in the [documentation/FAS-Simulator.pdf](https://github.com/keskival/FAS-Simulator/raw/master/documentation/FAS-Simulator.pdf).

See Executive summary poster in: [documentation/ExecutiveSummary.pdf](https://github.com/keskival/FAS-Simulator/raw/master/documentation/ExecutiveSummary.pdf).

It contains several pre-configured scripts for different kinds of production runs, named: `run*.py`

See Python dependencies from `requirements.txt`. For plotting things you need Octave and epstool.

Example: Running a simple simulation with a simulated wear and tear fault:
`./run_easy_with_wear_and_tear_fault.py`

Running the simulations produces output to the STDOUT, but the actual output is written as JSON to [output.json](https://github.com/keskival/FAS-Simulator/blob/master/data/output_easy_with_wear_and_tear_fault.json).

The output contains a sequence of events with timestamps.

Additionally, there are several `*.m` files and `*.sh` files in `utils` directory to create different kinds of visualizations
out of this JSON output using Octave and ffmepg.

The `data.mat` file for the Octave scripts is created using `./utils/output_to_octave.py`
from `output.json` to `data.mat`.

There is a baseline implementation using Hidden Markov Models for anomaly detection in: [fas_hmm](https://github.com/keskival/fas_hmm)

There is also a related FAS-Tensorflow project (private at the moment) that is an implementation that extracts process model
features from inputs generated by this project using deep learning methods, and uses those for anomaly detection. This is about a novel deep learning architecture which leverages interlaced sequential symmetry in the data.

## The Default Assembly Process Being Simulated

Step | Description | Duration | Log messages
--- | --- | --- | ---
1 | Crane | 30 s | Going forward, stopping, going back, stopping
2 | Manual inspection | 37 s | OK pressed, queue alarm
3 | Conveyor | 30 s | To station, stop, to next station
4 | Bowl feeder gives components | 5 s | Given
5 | Add components | 21 s | OK pressed, queue alarm
6 | Conveyor | 30 s | To station, stop, to next station
7 | Bowl feeder gives components | 10 s | Given
8 | Add components | 34 s | OK pressed, queue alarm
9 | Conveyor | 30 s | To station, stop, to next station
10 | Crane with subassembly A | 10 s | Going forward, stopping, going back, stopping
11 | Combine with subassembly A | 34 s | OK pressed, queue alarm
12 | Conveyor | 30 s | To station, stop, to next station
13 | Conveyor with subassembly B | 10 s | To station, stop
14 | Combine with subassembly B | 35 s | OK pressed, queue alarm
15 | Conveyor | 30 s | To station, stop, to next station
16 | Bowl feeder gives components | 5 s | Given
17 | Conveyor with cover | 10 s | To station, stop
18 | Add cover and bolts | 76 s | OK pressed, queue alarm
19 | Conveyor | 30 s | To station, stop, to next station
20 | Tighten the bolts | 28 s | OK pressed, queue alarm
21 | Conveyor | 30 s | To station, stop, to next station
22 | Conveyor with subassembly C | 10 s | To station, stop
23 | Combine with subassembly C | 60 s | OK pressed, queue alarm
24 | Conveyor | 21 s | To station, stop, to next station
25 | Tighten the bolts | 16 s | OK pressed, queue alarm
26 | Conveyor | 21 s | To station, stop, to next station
27 | Bowl feeder gives components | 5 s | Given
28 | Add components | 11 s | OK pressed, queue alarm
29 | Conveyor | 21 s | To station, stop, to next station
30 | Tighten the bolts | 32 s | OK pressed, queue alarm
31 | Conveyor | 21 s | To output gate

## Events

Event id | Event name
--- | ---
0 | TICK
1 | CONVEYOR1 CONVEYOR_GATE
2 | CONVEYOR2 CONVEYOR_GATE
3 | CONVEYOR3 CONVEYOR_GATE
4 | CONVEYOR4 CONVEYOR_GATE
5 | CONVEYOR5 CONVEYOR_GATE
6 | CONVEYOR6 CONVEYOR_GATE
7 | CONVEYOR7 CONVEYOR_GATE
8 | CONVEYOR8 CONVEYOR_GATE
9 | CONVEYOR9 CONVEYOR_GATE
10 | CONVEYOR10 CONVEYOR_GATE
11 | CONVEYOR11 CONVEYOR_GATE
12 | CONVEYOR_INPUT_SUBASSEMBLY_B CONVEYOR_GATE
13 | CONVEYOR_INPUT_SUBASSEMBLY_C CONVEYOR_GATE
14 | BOWL1 GIVEN
15 | BOWL2 GIVEN
16 | BOWL3 GIVEN
17 | BOWL4 GIVEN
18 | CRANE1 FORWARD
19 | CRANE1 BACKWARD
20 | CRANE1 STOP
21 | CRANE_INPUT_SUBASSEMBLY_A FORWARD
22 | CRANE_INPUT_SUBASSEMBLY_A BACKWARD
23 | CRANE_INPUT_SUBASSEMBLY_A STOP
24 | MANUAL_INSPECTION QUEUE_ALARM
25 | MANUAL_INSPECTION OK
26 | MANUAL_ADD_COMPONENTS1 QUEUE_ALARM
27 | MANUAL_ADD_COMPONENTS1 OK
28 | MANUAL_ADD_COMPONENTS2 QUEUE_ALARM
29 | MANUAL_ADD_COMPONENTS2 OK
30 | MANUAL_COMBINE_SUBASSEMBLY_A QUEUE_ALARM
31 | MANUAL_COMBINE_SUBASSEMBLY_A OK
32 | MANUAL_COMBINE_SUBASSEMBLY_B QUEUE_ALARM
33 | MANUAL_COMBINE_SUBASSEMBLY_B OK
34 | MANUAL_ADD_COVER_AND_BOLTS QUEUE_ALARM
35 | MANUAL_ADD_COVER_AND_BOLTS OK
36 | MANUAL_TIGHTEN_BOLTS1 QUEUE_ALARM
37 | MANUAL_TIGHTEN_BOLTS1 OK
38 | MANUAL_COMBINE_SUBASSEMBLY_C QUEUE_ALARM
39 | MANUAL_COMBINE_SUBASSEMBLY_C OK
40 | MANUAL_TIGHTEN_BOLTS2 QUEUE_ALARM
41 | MANUAL_TIGHTEN_BOLTS2 OK
42 | MANUAL_ADD_COMPONENTS3 QUEUE_ALARM
43 | MANUAL_ADD_COMPONENTS3 OK
44 | MANUAL_TIGHTEN_BOLTS3 QUEUE_ALARM
45 | MANUAL_TIGHTEN_BOLTS3 OK

## Operating Modes

There are several runs implemented:
- Run without errors
- Wear and tear fault, where a Conveyor is affected by a progressive delay.
- Retry delay fault, where a BowlFeeder process suffers from failed feed randomly, but continues correctly when retried.

## Generating Challenge Dataset

For the challenge task we create a set of clean runs, and a set of runs with errors happening at the starting point in the run.

A suggested learning system can be trained or conditioned on a subset of clean runs, and tested whether it is able to discriminate between runs with errors and clean runs. Note that a system shouldn't be trained on the faulty runs, because the fault types and behaviors cannot be known in advance in practice.

We first produce 10,000 runs with errors and 10,000 similar runs without errors in JSON.

Do this by running: `./generate_datasets.py`.

The data will be generated in JSON form, one file per run in `data/correct_runs/*.json` and `data/runs_with_errors/*.json`.

This data can then be converted to numpy format by running: `./convert_datasets_to_numpy.py`.

The data will be generated in numpy form, one file per run in `numpy_data/correct_runs/*.npy` and `numpy_data/runs_with_errors/*.npy`.

## Citing

FAS Simulator

```
@article{keski2017simulator,
  title={A simulator for event-oriented data in flexible assembly system fault prediction},
  author={Keski-Valkama, Tero},
  journal={Procedia computer science},
  volume={119},
  pages={121--130},
  year={2017},
  publisher={Elsevier}
}
```

## Repository
- [https://github.com/keskival/FAS-Simulator](https://github.com/keskival/FAS-Simulator)
