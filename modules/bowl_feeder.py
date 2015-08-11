#!/usr/bin/python
from random_delay import delay

class BowlFeeder:
    """ This class represents the bowl feeders giving parts to the manual assembly steps. """
    def __init__(self, name, duration, scheduler, logger):
        self.duration = duration
        self.scheduler = scheduler
        self.logger = logger
        self.name = name
        self.state = "waiting"
        self.next_step = lambda: None
    def set_next(self, next_step):
        self.next_step = next_step
    def input(self):
        print self.name + ": give"
        self.state = "giving"
        self.scheduler.add(self.given, delay(self.duration, 5))
    def given(self):
        print self.name + ": given"
        self.logger.addMessage(self.name + " GIVEN");
        self.state = "waiting"
        self.next_step()
