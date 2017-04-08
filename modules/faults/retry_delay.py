import simpy
import numpy as np
from math import exp

class RetryDelay(simpy.Resource):
    """ This class represents the human operator retry delay type of fault. """
    def __init__(self, env, module):
        super(RetryDelay, self).__init__(env)
        self.t = 0
        self.env = env
        self.module = module

    def process(self):
        with self.request() as req:
            yield req
            self.t = self.t + 1
            print("FAULT: RETRY_DELAY")
            # (poissrnd((exp(t/5)-1)/4) * 0.2 + 1)
            # Note: The factor is zero-based so that it can be added as a separate delay.
            delay_factor = np.random.poisson((exp(t/5)-1)/4) * 0.2)
            yield self.env.timeout(self.add_delay(self.module.duration, delay_factor), 1)
        return

    def add_delay(self, delay, delay_factor):
        return delay * delay_factor

    def spawn(self):
        return self.env.process(self.process())
