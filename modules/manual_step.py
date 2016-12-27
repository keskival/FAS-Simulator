#!/usr/bin/python
import simpy
from modules.random_delay import delay

class ManualStep(simpy.Resource):
    """ This class represents the manual steps. """
    def __init__(self, name, duration, logger, env):
        super(ManualStep, self).__init__(env, capacity=1)
        self.duration = duration
        self.queue = 0
        self.logger = logger
        self.state = "waiting"
        self.name = name
        self.env = env

    def process(self):
        print(self.name + ": input")
        self.queue = self.queue + 1
        if (self.queue >= 5):
            self.logger.addMessage("QUEUE ALARM");
        with self.request() as req:
            yield req
            print(self.name + ": process")
            self.queue = self.queue - 1
            self.state = "running"
            yield self.env.timeout(delay(self.duration, 5))
            print(self.name + ": ok")
            self.logger.addMessage(self.name + " OK");
        print(self.name + ": wait")
        self.state = "waiting"
        return

    def spawn(self):
        return self.env.process(self.process())
    