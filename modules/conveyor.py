#!/usr/bin/python
from random_delay import delay

class Conveyor:
    """ This class represents the conveyors. The difference to cranes is that conveyors do not wait
        before processing the next item. There is no queue for the conveyor."""
    def __init__(self, name, duration, scheduler, logger):
        self.duration = duration
        self.scheduler = scheduler
        self.logger = logger
        self.name = name
        self.next_step = lambda: None
    def set_next(self, next_step):
        self.next_step = next_step
    def input(self):
        print self.name + ": input"
        self.logger.addMessage(self.name + " CONVEYOR GATE");
        self.scheduler.add(self.to_next_step, delay(self.duration, 5))
    def to_next_step(self):
        print self.name + ": to_next_step"
        self.next_step()
