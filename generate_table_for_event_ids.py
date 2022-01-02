#!/usr/bin/python3

from modules.process.production_line import ProductionLine
from modules.components.clock import Clock

# Getting all event types to make an index out of them.
production_line = ProductionLine(None, None, False)
clock = Clock(None, None, False)
all_event_types = clock.get_events() + production_line.get_events()

print("Event id | Event name")
print("--- | ---")
for id, event in enumerate(all_event_types):
    print(f"{id} | {event}")

print("""\\begin{table}[!t]
\\caption{Table of the Event Identifiers}
\\label{eventids}
\\centering
\\begin{tabular}{|p{5mm}|p{55mm}|}
\\hline
Event id & Event name \\\\
\\hline
\\hline""")
for id, event in enumerate(all_event_types):
    event = event.replace("_", "\\_")
    print(f"{id} & {event} \\\\")
    print("\\hline")
print("""\\end{tabular}
\\end{table}""")
