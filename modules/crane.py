#!/usr/bin/python
from random_delay import delay

class Crane:
    """ This class represents the cranes. """
    def __init__(self, name, duration, scheduler, logger):
        self.duration = duration
        self.queue = 0
        self.scheduler = scheduler
        self.logger = logger
        self.name = name
        self.state = "waiting"
        self.next_step = lambda: None
    def set_next(self, next_step):
        self.next_step = next_step
    def input(self):
        print self.name + ": input"
        self.queue = self.queue + 1
        if (self.state == "waiting"):
            self.go_forward()
    def go_forward(self):
        print self.name + ": go_forward"
        self.logger.addMessage(self.name + " FORWARD");
        self.queue = self.queue - 1
        self.state = "running"
        self.scheduler.add(self.stop, delay(self.duration, 5))
    def stop(self):
        print self.name + ": stop"
        self.logger.addMessage(self.name + " STOP");
        self.next_step()
    def item_taken(self):
        print self.name + ": item_taken"
        self.go_back()
    def go_back(self):
        print self.name + ": go_back"
        self.logger.addMessage(self.name + " BACKWARD");
        self.scheduler.add(self.wait, delay(self.duration, 5))
    def wait(self):
        print self.name + ": wait"
        self.logger.addMessage(self.name + " STOP");
        self.state = "waiting"
        if (self.queue > 0):
            self.go_forward()
