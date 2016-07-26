#!/usr/bin/python3

import simpy
from modules.production_line import ProductionLine
from modules.fas_instance import FASInstance

from logger import Logger

# Initializing
env = simpy.Environment()

logger = Logger(env)

production_line = ProductionLine(env, logger)

# Putting in 30 items, waiting for them to be done.

for i in range(0, 30):
    fas_instance = FASInstance(env, production_line, logger)
    fas_instance.spawn()

env.run()

print("Done.")

f = open('output.json', 'w')
f.write(logger.getLoglines())
f.close()
