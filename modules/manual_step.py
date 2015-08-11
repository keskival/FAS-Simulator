#!/usr/bin/python
from random_delay import delay

class ManualStep:
    """ This class represents the manual steps. """
    def __init__(self, name, duration, scheduler, logger):
        self.duration = duration
        self.queue = 0
        self.scheduler = scheduler
        self.logger = logger
        self.state = "waiting"
        self.name = name
        self.next_step = lambda: None
    def set_next(self, next_step):
        self.next_step = next_step
    def input(self):
        print self.name + ": input"
        self.queue = self.queue + 1
        if (self.state == "waiting"):
            self.process()
    def process(self):
        print self.name + ": process"
        self.queue = self.queue - 1
        self.state = "running"
        self.scheduler.add(self.ok, delay(self.duration, 30))
    def ok(self):
        print self.name + ": ok"
        self.logger.addMessage(self.name + " OK");
        self.next_step()
        self.wait()
    def wait(self):
        print self.name + ": wait"
        self.state = "waiting"
        if (self.queue > 0):
            self.process()
