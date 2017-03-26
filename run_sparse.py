#!/usr/bin/python3

import simpy
from modules.production_line import ProductionLine
from modules.fas_instance import FASInstance
from modules.clock import Clock

from logger import Logger

# Initializing
env = simpy.Environment()

logger = Logger(env)

production_line = ProductionLine(env, logger)

clock = Clock(logger, env)
clock.spawn()

# Doing a couple of global repeats

for i in range(0,20):

    # First running through with one item.

    fas_instance = FASInstance(env, production_line, logger)
    fas_instance.spawn()
    env.run()
    
    # Then 2 items spaced a bit.
    
    fas_instance = FASInstance(env, production_line, logger)
    fas_instance.spawn()
    
    for j in range(0, 5):
        env.step()
    
    fas_instance = FASInstance(env, production_line, logger)
    fas_instance.spawn()
    
    env.run()
    
    # Then 2 items spaced more.
    
    fas_instance = FASInstance(env, production_line, logger)
    fas_instance.spawn()
    
    for j in range(0, 8):
        env.step()
    
    fas_instance = FASInstance(env, production_line, logger
    fas_instance.spawn()
    
    env.run()
    
    # Then 2 items spaced less.
    
    fas_instance = FASInstance(env, production_line, logger)
    fas_instance.spawn()
    
    for j in range(0, 3):
        env.step()
    
    fas_instance = FASInstance(env, production_line, logger)
    fas_instance.spawn()
    
    env.run()
    
    # Then 3 items spaced a bit.
    
    fas_instance = FASInstance(env, production_line, logger)
    fas_instance.spawn()
    
    for j in range(0, 5):
        env.step()
    
    fas_instance = FASInstance(env, production_line, logger)
    fas_instance.spawn()
    
    for j in range(0, 5):
        env.step()
    
    fas_instance = FASInstance(env, production_line, logger)
    last_item = fas_instance.spawn()
    
    env.run(last_item)

print("Done.")

f = open('output.json', 'w')
f.write(logger.getLoglines())
f.close()
