import simpy
from modules.process.random_delay import delay

class Crane(simpy.Resource):
    """ This class represents the cranes. They transport one item at a time. """
    def __init__(self, name, duration, logger, env, debug=True):
        super(Crane, self).__init__(env, capacity=1)
        self.debug = debug
        self.duration = duration
        self.queue = 0
        self.logger = logger
        self.name = name
        self.state = "waiting"
        self.env = env

    def process(self):
        if self.debug:
            print(self.name + ": input")
        self.queue = self.queue + 1
        with self.request() as req:
            yield req
            if self.debug:
                print(self.name + ": go_forward")
            self.logger.addMessage(self.name + " FORWARD");
            self.queue = self.queue - 1
            self.state = "running"
            yield self.env.timeout(delay(self.duration, 1))
            if self.debug:
                print(self.name + ": wait")
            self.state = "waiting"
            if self.debug:
                print(self.name + ": item_taken")
                print(self.name + ": go_back")
            self.logger.addMessage(self.name + " BACKWARD");
            yield self.env.timeout(delay(self.duration, 1))
            if self.debug:
                print(self.name + ": stop")
            self.logger.addMessage(self.name + " STOP");
        return

    def spawn(self):
        return self.env.process(self.process())
