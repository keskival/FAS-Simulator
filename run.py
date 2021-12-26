#!/usr/bin/python3

import simpy
from modules.process.production_line import ProductionLine
from modules.process.fas_instance import FASInstance
from modules.components.clock import Clock

from simulator.logger import Logger

# Initializing
env = simpy.Environment()

logger = Logger(env)

production_line = ProductionLine(env, logger)

# First running through with one item for debugging reasons, to make sure the
# event indices follow this order.

fas_instance = FASInstance(env, production_line, logger)
clock = Clock(env, logger)
done = fas_instance.spawn()
clock.spawn()
env.run(done)

# Putting in 20 items, waiting for them to be done, and then putting in 50 more,
# waiting them to be done also.

for i in range(0, 20):
    fas_instance = FASInstance(env, production_line, logger)
    done = fas_instance.spawn()

env.run(done)

for j in range(0, 50):
    fas_instance = FASInstance(env, production_line, logger)
    done = fas_instance.spawn()

env.run(done)

print("Done.")

f = open("data/output.json", "w")
f.write(logger.getLoglines())
f.close()
