#!/usr/bin/python
from random_delay import delay

class Crane:
    """ This class is a base class for all the cranes. """
    def __init__(self, duration, scheduler, next_step):
        self.duration = duration
        self.queue = 0
        self.scheduler = scheduler
        self.state = "waiting"
        self.next_step = next_step
    def add_queue(self):
        print "add_queue"
        self.queue = self.queue + 1
        if (self.state == "waiting"):
            self.go_forward()
    def go_forward(self):
        print "go_forward"
        self.queue = self.queue - 1
        self.state = "running"
        self.scheduler.add(self.stop, delay(self.duration, 5))
    def stop(self):
        print "stop"
        self.next_step()
    def item_taken(self):
        print "item_taken"
        self.go_back()
    def go_back(self):
        print "go_back"
        self.scheduler.add(self.wait, delay(self.duration, 5))
    def wait(self):
        print "wait"
        self.state = "waiting"
        if (self.queue > 0):
            self.go_forward()
