import simpy
import numpy as np
from math import exp

class RetryDelay(simpy.Resource):
    """
    This class represents the human operator retry delay type of fault.
    Simulated RetryDelay faults only apply to BowlFeeders.
    """
    def __init__(self, env, module, debug=True):
        super(RetryDelay, self).__init__(env)
        self.t = 0
        self.env = env
        self.module = module
        self.debug = debug

    def process(self):
        with self.request() as req:
            yield req
            self.t = self.t + 1
            # (poissrnd((exp(t/5)-1)/4) * 0.2 + 1)
            # Note: The factor is zero-based so that it can be added as a separate delay.
            delay_factor = np.random.poisson((exp(self.t/5)-1)/4) * 0.2
            if self.debug:
                print("FAULT: RETRY_DELAY: ", delay_factor)
            yield self.env.timeout(self.add_delay(self.module.duration, delay_factor), 1)
        return

    def add_delay(self, delay, delay_factor):
        return delay * delay_factor

    def spawn(self):
        return self.env.process(self.process())
