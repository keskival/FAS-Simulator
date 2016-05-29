#!/usr/bin/python
import simpy
from modules.random_delay import delay

class Conveyor(simpy.Resource):
    """ This class represents the conveyors. The difference to cranes is that conveyors do not wait
        before processing the next item. There is no queue for the conveyor."""
    def __init__(self, name, duration, logger, env):
        super(Conveyor, self).__init__(env)
        self.duration = duration
        self.logger = logger
        self.name = name
        self.env = env
    def process(self):
        with self.request() as req:
            yield req
            print(self.name + ": input")
            self.logger.addMessage(self.name + " CONVEYOR GATE");
            yield self.env.timeout(delay(self.duration, 5))
        print(self.name + ": to_next_step")
        return

    def spawn(self):
        return self.env.process(self.process())
