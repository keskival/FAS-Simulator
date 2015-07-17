#!/usr/bin/python

from modules.crane import Crane
from scheduler import Scheduler

# Testing
scheduler = Scheduler()
crane1 = Crane(30000, scheduler, lambda: scheduler.add(crane1.item_taken, 0))
crane1.add_queue()
crane1.add_queue()
while scheduler.next():
    pass
print "Done."
