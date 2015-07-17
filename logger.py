#!/usr/bin/python

from logline import LogLine

class Logger:
    """ This class logs all the messages. """
    def __init__(self, scheduler):
        self.scheduler = scheduler
        self.loglines = []
    def addMessage(self, type, metadata = ""):
        logline = LogLine(self.scheduler.time, type, metadata)
        self.loglines.append(logline)
    def getLoglines(self):
        return ",\n".join(map(str, self.loglines))
