# FAS Simulator
A modular benchmark simulator for flexible assembly systems.

Licence: WTFPL

This project includes a SimPy discrete event simulator simulating a plausible Flexible Assembly System
documented in the [documentation/FAS-Simulator.pdf](https://github.com/keskival/FAS-Simulator/raw/master/documentation/FAS-Simulator.pdf).

It contains several pre-configured scripts for different kinds of production runs, named: `run*.py`

Example: Running a simple simulation with a simulated wear and tear fault:
`./run_easy_with_fault.py`

Running the simulations produces output to the STDOUT, but the actual output is written as JSON to `output.json`.

The output contains a sequence of events with timestamps.
