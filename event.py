#!/usr/bin/python

class Event:
    """ An event. """
    def __init__(self, timestamp, callback):
        self.timestamp = timestamp
        self.callback = callback
    def __cmp__(self, other):
        return cmp(self.timestamp, other.timestamp)
    def execute(self):
        self.callback()
