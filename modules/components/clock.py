import simpy
from modules.process.random_delay import delay

class Clock():
    """ Models a periodical tick event for every 10 seconds. """
    def __init__(self, logger, env, debug=True):
        self.debug = debug
        self.logger = logger
        self.env = env

    def process(self):
        while True:
            if self.debug:
                print("Tick")
            self.logger.addMessage("TICK");
            yield self.env.timeout(10000)

    def spawn(self):
        return self.env.process(self.process())
