#!/usr/bin/python
import simpy
from modules.random_delay import delay

from modules.bowl_feeder import BowlFeeder
from modules.conveyor import Conveyor
from modules.crane import Crane
from modules.manual_step import ManualStep

# Models one production line
class ProductionLine:
    def __init__(self, env, logger):
        self.env = env
        # The modules of the assembly line are created here in order, but wired together in the process definition.
        # All these are simpy resources with a limited capacity.
        self.input = simpy.resources.store.Store(env)
        self.crane1 = Crane("CRANE1", 30000, logger, env)
        self.manual_inspection = ManualStep("MANUAL_INSPECTION", 37000, logger, env)
        self.conveyor1 = Conveyor("CONVEYOR1", 30000, logger, env)
        self.bowl1 = BowlFeeder("BOWL1", 5000, logger, env)
        self.manual_add_components1 = ManualStep("MANUAL_ADD_COMPONENTS1", 21000, logger, env)
        self.conveyor2 = Conveyor("CONVEYOR2", 30000, logger, env)
        self.bowl2 = BowlFeeder("BOWL2", 10000, logger, env)
        self.manual_add_components2 = ManualStep("MANUAL_ADD_COMPONENTS2", 34000, logger, env)
        self.conveyor3 = Conveyor("CONVEYOR3", 30000, logger, env)
        self.input_subassembly_a = simpy.resources.store.Store(env)
        self.crane_input_subassembly_a = Crane("CRANE_INPUT_SUBASSEMBLY_A", 10000, logger, env)
        self.manual_combine_subassembly_a = ManualStep("MANUAL_COMBINE_SUBASSEMBLY_A", 34000, logger, env)
        self.conveyor4 = Conveyor("CONVEYOR4", 30000, logger, env)
        self.input_subassembly_b = simpy.resources.store.Store(env)
        self.conveyor_input_subassembly_b = Conveyor("CONVEYOR_INPUT_SUBASSEMBLY_B", 10000, logger, env)
        self.manual_combine_subassembly_b = ManualStep("MANUAL_COMBINE_SUBASSEMBLY_B", 35000, logger, env)
        self.conveyor6 = Conveyor("CONVEYOR6", 30000, logger, env)
        self.bowl3 = BowlFeeder("BOWL3", 5000, logger, env)
        self.conveyor7 = Conveyor("CONVEYOR7", 10000, logger, env)
        self.manual_add_cover_and_bolts = ManualStep("MANUAL_ADD_COVER_AND_BOLTS", 76000, logger, env)
        self.conveyor8 = Conveyor("CONVEYOR8", 30000, logger, env)
        self.manual_tighten_bolts1 = ManualStep("MANUAL_TIGHTEN_BOLTS1", 28000, logger, env)
        self.conveyor9 = Conveyor("CONVEYOR9", 30000, logger, env)
        self.input_subassembly_c = simpy.resources.store.Store(env)
        self.conveyor_input_subassembly_c = Conveyor("CONVEYOR_INPUT_SUBASSEMBLY_C", 10000, logger, env)
        self.manual_combine_subassembly_c = ManualStep("MANUAL_COMBINE_SUBASSEMBLY_C", 60000, logger, env)
        self.conveyor11 = Conveyor("CONVEYOR11", 21000, logger, env)
        self.manual_tighten_bolts2 = ManualStep("MANUAL_TIGHTEN_BOLTS2", 16000, logger, env)
        self.conveyor12 = Conveyor("CONVEYOR12", 21000, logger, env)
        self.bowl4 = BowlFeeder("BOWL4", 5000, logger, env)
        self.manual_add_components3 = ManualStep("MANUAL_ADD_COMPONENTS3", 11000, logger, env)
        self.conveyor13 = Conveyor("CONVEYOR13", 21000, logger, env)
        self.manual_tighten_bolts3 = ManualStep("MANUAL_TIGHTEN_BOLTS3", 32000, logger, env)
        self.conveyor14 = Conveyor("CONVEYOR14", 21000, logger, env)
        self.output = simpy.resources.store.Store(env)
