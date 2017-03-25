import simpy
from math import exp

class WearAndTear(simpy.Resource):
    """ This class represents the wear and tear type of fault. """
    def __init__(self, env, module):
        super(WearAndTear, self).__init__(env)
        self.t = 0
        self.env = env
        self.module = module
        self.name = "FAULT: WEAR_AND_TEAR"

    def process(self):
        with self.request() as req:
            yield req
            self.t = self.t + 1
            print("WearAndTear")
            delay_factor = (exp(self.t/5.0) - 1 ) / 30
            yield self.env.timeout(self.add_delay(self.module.duration, delay_factor), 1)
        print(self.name + ": to_next_step")
        return

    def add_delay(self, delay, delay_factor):
        # Note: The factor is zero-based so that it can be added as a separate delay.
        return delay * delay_factor

    def spawn(self):
        return self.env.process(self.process())
