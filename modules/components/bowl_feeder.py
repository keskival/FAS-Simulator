import simpy
from modules.process.random_delay import delay

class BowlFeeder(simpy.Resource):
    """
    This class represents the bowl feeders giving parts to the manual
    assembly steps.
    Simulated RetryDelay faults only apply to BowlFeeders.
    """
    def __init__(self, name, duration, logger, env, debug=True):
        super(BowlFeeder, self).__init__(env, capacity=1)
        self.debug = debug
        self.duration = duration
        self.logger = logger
        self.name = name
        self.state = "waiting"
        self.env = env
        self.faults = []

    def add_fault(self, fault):
        self.faults.append(fault)

    def process(self):
        with self.request() as req:
            yield req
            if self.debug:
                print(self.name + ": give")
            self.state = "giving"
            yield self.env.timeout(delay(self.duration, 1))
            for fault in self.faults:
                yield fault.spawn()
            if self.debug:
                print(self.name + ": given")
            self.logger.addMessage(self.name + " GIVEN");
        self.state = "waiting"
        return

    def spawn(self):
        return self.env.process(self.process())
