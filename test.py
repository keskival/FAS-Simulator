#!/usr/bin/python3

from modules.crane import Crane
from modules.manual_step import ManualStep
from scheduler import Scheduler
from logger import Logger

# Testing
scheduler = Scheduler()
logger = Logger(scheduler)
manual_step1 = ManualStep("MANUAL_STEP1", 37000, scheduler, logger, lambda: None)

def passToManualStep1():
    scheduler.add(crane1.item_taken, 0)
    scheduler.add(manual_step1.add_queue, 0)
    
crane1 = Crane("CRANE1", 30000, scheduler, logger, passToManualStep1)
crane1.add_queue()
crane1.add_queue()
while scheduler.next():
    pass
print "Done."
print logger.getLoglines()
