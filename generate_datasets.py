#!/usr/bin/python3

import simpy
import os
import random

from modules.process.production_line import ProductionLine
from modules.process.fas_instance import FASInstance
from modules.faults.wear_and_tear import WearAndTear
from modules.faults.retry_delay import RetryDelay
from modules.components.clock import Clock

from simulator.logger import Logger

def generate_run(filename, fault=None):
    # Initializing
    env = simpy.Environment()

    logger = Logger(env)

    production_line = ProductionLine(env, logger, False)

    clock = Clock(env, logger, False)
    clock.spawn()

    if fault is not None:
        # Adding a fault immediately.
        env.process(fault(env, production_line))

    # Putting in 30 items, waiting for them to be done.

    last_item = None

    for i in range(0, 30):
        fas_instance = FASInstance(env, production_line, logger)
        last_item = fas_instance.spawn()

    env.run(last_item)

    f = open(filename, "w")
    f.write(logger.getLoglines())
    f.close()

def add_wear_and_tear_fault(env, production_line):
    yield env.timeout(0)
    # Simulated WearAndTear faults only apply to Conveyors.
    conveyor_to_fail = random.sample(production_line.conveyors, 1)[0]
    conveyor_to_fail.add_fault(
        WearAndTear(env, conveyor_to_fail, False));

def add_retry_delay_fault(env, production_line):
    yield env.timeout(0)
    # Simulated RetryDelay faults only apply to BowlFeeders.
    bowl_feeder_to_fail = random.sample(production_line.bowl_feeders, 1)[0]
    bowl_feeder_to_fail.add_fault(
        RetryDelay(env, bowl_feeder_to_fail, False));

NUMBER_OF_RUNS = 100000

os.makedirs("data/runs_with_errors", exist_ok=True)
os.makedirs("data/correct_runs", exist_ok=True)

for run in range(NUMBER_OF_RUNS):
    print(f"Generating correct run {run}/{NUMBER_OF_RUNS}")
    generate_run(f"data/correct_runs/{run}.json", None)

for run in range(NUMBER_OF_RUNS):
    print(f"Generating faulty run {run}/{NUMBER_OF_RUNS}")
    fault_types = [add_wear_and_tear_fault, add_retry_delay_fault]
    fault = random.sample(fault_types, 1)[0]
    generate_run(f"data/runs_with_errors/{run}.json", fault)
