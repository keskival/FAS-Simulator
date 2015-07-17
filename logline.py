#!/usr/bin/python

class LogLine:
    """ A class that represent log lines. """
    def __init__(self, timestamp, type, metadata):
        self.timestamp = timestamp
        self.type = type
        self.metadata = metadata