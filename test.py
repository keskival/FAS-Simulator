#!/usr/bin/python

from modules.crane import Crane
from scheduler import Scheduler

# Testing
scheduler = Scheduler()
crane1 = Crane(30000, scheduler)
crane1.add_queue()
crane1.add_queue()
scheduler.add(lambda: crane1.item_taken(), 100000)
print "Scheduling next event."
while scheduler.next():
    print "Scheduling next event."
print "Done."
