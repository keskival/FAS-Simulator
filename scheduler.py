#!/usr/bin/python

import bisect
from event import Event
 
class Scheduler:
    """A scheduler object which takes in new events to be scheduled and fires them in chronological order."""
    def __init__(self):
        self.time = 0
        self.events = []
    def next(self):
        print "Scheduling at time: " + str(self.time)
        if (len(self.events) == 0):
            return False
        else:
            next_event = self.events.pop(0)
            self.time = next_event.timestamp
            # Executing the next event.
            next_event.execute()
            return True
    def add(self, callback, delay):
        event = Event(self.time + delay, callback)
        bisect.insort(self.events, event)

# Testing
if __name__ == "__main__":
    scheduled = []
    scheduler = Scheduler()
    def do_event1():
        scheduled.append("event1")
    def do_event2():
        scheduled.append("event2")
    scheduler.add(do_event2, 100)
    scheduler.add(do_event1, 0)
    ok = scheduler.next()
    if (not ok):
        raise Exception("Scheduler failed at 1.")
    if (scheduled != ["event1"]):
        raise Exception("An incorrect event was scheduled! " + str(scheduled))
    ok = scheduler.next()
    if (not ok):
        raise Exception("Scheduler failed at 2.")
    if (scheduled != ["event1", "event2"]):
        raise Exception("An incorrect event was scheduled! " + str(scheduled))
    ok = scheduler.next()
    if (ok):
        raise Exception("Scheduler should have failed at the end.")
    print "Test ok!"
