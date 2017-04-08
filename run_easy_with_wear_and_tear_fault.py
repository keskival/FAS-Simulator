#!/usr/bin/python3

import simpy
from modules.process.production_line import ProductionLine
from modules.process.fas_instance import FASInstance
from modules.faults.wear_and_tear import WearAndTear
from modules.components.clock import Clock

from simulator.logger import Logger

# Initializing
env = simpy.Environment()

logger = Logger(env)

production_line = ProductionLine(env, logger)

clock = Clock(logger, env)
clock.spawn()

# Adding a fault on a timeout
def fault():
    yield env.timeout(10000)
    print("FAULT")
    production_line.conveyor_input_subassembly_b.add_fault(
        WearAndTear(env, production_line.conveyor_input_subassembly_b));
env.process(fault())

# Putting in 30 items, waiting for them to be done.

last_item = None

for i in range(0, 30):
    fas_instance = FASInstance(env, production_line, logger)
    last_item = fas_instance.spawn()

env.run(last_item)

print("Done.")

f = open("data/output_easy_with_wear_and_tear_fault.json", "w")
f.write(logger.getLoglines())
f.close()
