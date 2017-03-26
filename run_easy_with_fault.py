#!/usr/bin/python3

import simpy
from modules.production_line import ProductionLine
from modules.fas_instance import FASInstance
from modules.wear_and_tear import WearAndTear
from modules.clock import Clock

from logger import Logger

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

f = open('output.json', 'w')
f.write(logger.getLoglines())
f.close()
