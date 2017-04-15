import simpy
from math import exp

class WearAndTear(simpy.Resource):
    """ This class represents the wear and tear type of fault. """
    def __init__(self, env, module):
        super(WearAndTear, self).__init__(env)
        self.t = 0
        self.env = env
        self.module = module

    def process(self):
        with self.request() as req:
            yield req
            self.t = self.t + 1
            # ((exp(t / 5.0) - 1) / 30 + 1)
            # Note: The factor is zero-based so that it can be added as a separate delay.
            delay_factor = (exp(self.t/5.0) - 1 ) / 30
            extra_delay = delay_factor * self.module.duration
            print("FAULT: WEAR_AND_TEAR ", extra_delay)
            yield self.env.timeout(extra_delay)
        return

    def spawn(self):
        return self.env.process(self.process())
