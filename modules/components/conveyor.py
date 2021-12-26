import simpy
from modules.process.random_delay import delay

class Conveyor(simpy.Resource):
    """
    This class represents the conveyors. The difference to cranes is that conveyors do not wait
    before processing the next item. There is no queue for the conveyor.
    Simulated WearAndTear faults only apply to Conveyors.
    """
    def __init__(self, name, duration, logger, env, debug=True):
        super(Conveyor, self).__init__(env)
        self.debug = debug
        self.duration = duration
        self.logger = logger
        self.name = name
        self.env = env
        self.faults = []

    def add_fault(self, fault):
        self.faults.append(fault)

    def process(self):
        with self.request() as req:
            yield req
            if self.debug:
                print(self.name + ": input")
            self.logger.addMessage(self.name + " CONVEYOR GATE");
            yield self.env.timeout(delay(self.duration, 1))
            for fault in self.faults:
                yield fault.spawn()
        if self.debug:
            print(self.name + ": to_next_step")
        return

    def spawn(self):
        return self.env.process(self.process())

    def get_events(self):
        return [self.name + " CONVEYOR GATE"]
