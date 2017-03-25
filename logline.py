class LogLine:
    """ A class that represent log lines. """
    def __init__(self, timestamp, msgtype, metadata):
        self.timestamp = timestamp
        self.msgtype = msgtype
        self.metadata = metadata
    def __str__(self):
        return "{\n  \"timestamp\": " + str(self.timestamp) + ",\n  \"type\": \"" + self.msgtype + "\"\n}"
