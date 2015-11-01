#!/usr/bin/python

from modules.bowl_feeder import BowlFeeder
from modules.conveyor import Conveyor
from modules.crane import Crane
from modules.manual_step import ManualStep

from scheduler import Scheduler
from logger import Logger

# Initializing
scheduler = Scheduler()
logger = Logger(scheduler)
step = range(0, 32)

step[1] = Crane("CRANE1", 30000, scheduler, logger)
step[2] = ManualStep("MANUAL_INSPECTION", 37000, scheduler, logger)
step[3] = Conveyor("CONVEYOR1", 30000, scheduler, logger)
step[4] = BowlFeeder("BOWL1", 5000, scheduler, logger)
step[5] = ManualStep("MANUAL_ADD_COMPONENTS1", 21000, scheduler, logger)
step[6] = Conveyor("CONVEYOR2", 30000, scheduler, logger)
step[7] = BowlFeeder("BOWL2", 10000, scheduler, logger)
step[8] = ManualStep("MANUAL_ADD_COMPONENTS2", 34000, scheduler, logger)
step[9] = Conveyor("CONVEYOR3", 30000, scheduler, logger)
step[10] = Crane("CRANE_INPUT_SUBASSEMBLY_A", 10000, scheduler, logger)
step[11] = ManualStep("MANUAL_COMBINE_SUBASSEMBLY_A", 34000, scheduler, logger)
step[12] = Conveyor("CONVEYOR4", 30000, scheduler, logger)
step[13] = Conveyor("CONVEYOR_INPUT_SUBASSEMBLY_B", 10000, scheduler, logger)
step[14] = ManualStep("MANUAL_COMBINE_SUBASSEMBLY_B", 35000, scheduler, logger)
step[15] = Conveyor("CONVEYOR6", 30000, scheduler, logger)
step[16] = BowlFeeder("BOWL3", 5000, scheduler, logger)
step[17] = Conveyor("CONVEYOR7", 10000, scheduler, logger)
step[18] = ManualStep("MANUAL_ADD_COVER_AND_BOLTS", 76000, scheduler, logger)
step[19] = Conveyor("CONVEYOR8", 30000, scheduler, logger)
step[20] = ManualStep("MANUAL_TIGHTEN_BOLTS1", 28000, scheduler, logger)
step[21] = Conveyor("CONVEYOR9", 30000, scheduler, logger)
step[22] = Conveyor("CONVEYOR_INPUT_SUBASSEMBLY_C", 10000, scheduler, logger)
step[23] = ManualStep("MANUAL_COMBINE_SUBASSEMBLY_C", 60000, scheduler, logger)
step[24] = Conveyor("CONVEYOR11", 21000, scheduler, logger)
step[25] = ManualStep("MANUAL_TIGHTEN_BOLTS2", 16000, scheduler, logger)
step[26] = Conveyor("CONVEYOR12", 21000, scheduler, logger)
step[27] = BowlFeeder("BOWL4", 5000, scheduler, logger)
step[28] = ManualStep("MANUAL_ADD_COMPONENTS3", 11000, scheduler, logger)
step[29] = Conveyor("CONVEYOR13", 21000, scheduler, logger)
step[30] = ManualStep("MANUAL_TIGHTEN_BOLTS3", 32000, scheduler, logger)
step[31] = Conveyor("CONVEYOR14", 21000, scheduler, logger)

def passToStep2():
    scheduler.add(step[1].item_taken, 0)
    scheduler.add(step[2].input, 0)
step[1].set_next(passToStep2)

def passToStep3():
    scheduler.add(step[3].input, 0)
step[2].set_next(passToStep3)

def passToStep4():
    scheduler.add(step[4].input, 0)
step[3].set_next(passToStep4)

def passToStep5():
    scheduler.add(step[5].input, 0)
step[4].set_next(passToStep5)

def passToStep6():
    scheduler.add(step[6].input, 0)
step[5].set_next(passToStep6)

def passToStep7():
    scheduler.add(step[7].input, 0)
step[6].set_next(passToStep7)

def passToStep8():
    scheduler.add(step[8].input, 0)
step[7].set_next(passToStep8)

def passToStep9():
    scheduler.add(step[9].input, 0)
step[8].set_next(passToStep9)

def passToStep10():
    scheduler.add(step[10].input, 0)
step[9].set_next(passToStep10)

def passToStep11():
    scheduler.add(step[10].item_taken, 0)
    scheduler.add(step[11].input, 0)
step[10].set_next(passToStep11)

def passToStep12():
    scheduler.add(step[12].input, 0)
step[11].set_next(passToStep12)

def passToStep13():
    scheduler.add(step[13].input, 0)
step[12].set_next(passToStep13)

def passToStep14():
    scheduler.add(step[14].input, 0)
step[13].set_next(passToStep14)

def passToStep15():
    scheduler.add(step[15].input, 0)
step[14].set_next(passToStep15)

def passToStep16():
    scheduler.add(step[16].input, 0)
step[15].set_next(passToStep16)

def passToStep17():
    scheduler.add(step[17].input, 0)
step[16].set_next(passToStep17)

def passToStep18():
    scheduler.add(step[18].input, 0)
step[17].set_next(passToStep18)

def passToStep19():
    scheduler.add(step[19].input, 0)
step[18].set_next(passToStep19)

def passToStep20():
    scheduler.add(step[20].input, 0)
step[19].set_next(passToStep20)

def passToStep21():
    scheduler.add(step[21].input, 0)
step[20].set_next(passToStep21)

def passToStep22():
    scheduler.add(step[22].input, 0)
step[21].set_next(passToStep22)

def passToStep23():
    scheduler.add(step[23].input, 0)
step[22].set_next(passToStep23)

def passToStep24():
    scheduler.add(step[24].input, 0)
step[23].set_next(passToStep24)

def passToStep25():
    scheduler.add(step[25].input, 0)
step[24].set_next(passToStep25)

def passToStep26():
    scheduler.add(step[26].input, 0)
step[25].set_next(passToStep26)

def passToStep27():
    scheduler.add(step[27].input, 0)
step[26].set_next(passToStep27)

def passToStep28():
    scheduler.add(step[28].input, 0)
step[27].set_next(passToStep28)

def passToStep29():
    scheduler.add(step[29].input, 0)
step[28].set_next(passToStep29)

def passToStep30():
    scheduler.add(step[30].input, 0)
step[29].set_next(passToStep30)

def passToStep31():
    scheduler.add(step[31].input, 0)
step[30].set_next(passToStep31)

# First running through with one item for debugging reasons, to make sure the
# event indices follow this order.

step[1].input()

while scheduler.next():
    pass

# Putting in 20 items, waiting for them to be done, and then putting in 50 more,
# waiting them to be done also.

for i in range(0, 20):
    step[1].input()

while scheduler.next():
    pass

for j in range(0, 50):
    step[1].input()

while scheduler.next():
    pass

print "Done."

f = open('output.json', 'w')
f.write(logger.getLoglines())
f.close()
