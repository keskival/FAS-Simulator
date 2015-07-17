#!/usr/bin/python

import bisect

class Scheduler:
    """A scheduler object which takes in new events to be scheduled and fires them in chronological order."""
    def __init__(self):
        self.time = 0
        self.events = []
    def next(self):
        if (len(self.events) == 0):
            return False
        else:
            next_event = self.events.pop(0)
            # Executing the next event. This gives the scheduler as a parameter
            # so that the event can add new events.
            next_event.execute(self)
            return True
    def add(self, event):
        bisect.insort(self.events, event)

# Testing
if __name__ == "__main__":
    from event import Event
    scheduled = []
    scheduler = Scheduler()
    def do_event1(schd):
        if (schd != scheduler):
            raise Exception("Scheduler was not passed correctly!")
        scheduled.append("event1")
    def do_event2(schd):
        if (schd != scheduler):
            raise Exception("Scheduler was not passed correctly!")
        scheduled.append("event2")
    event1 = Event(0, do_event1)
    event2 = Event(100, do_event2)
    scheduler.add(event2)
    scheduler.add(event1)
    ok = scheduler.next()
    if (not ok):
        raise Exception("Scheduler failed at 1.")
    if (scheduled != ["event1"]):
        raise Exception("An incorrect event was scheduled! " + scheduled)
    ok = scheduler.next()
    if (not ok):
        raise Exception("Scheduler failed at 2.")
    if (scheduled != ["event1", "event2"]):
        raise Exception("An incorrect event was scheduled! " + scheduled)
    ok = scheduler.next()
    if (ok):
        raise Exception("Scheduler should have failed at the end.")
    print "Test ok!"
