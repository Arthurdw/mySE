from json import loads
from datetime import datetime


class Log:
    def __init__(self, log):
        self.log = log

    @property
    def id(self):
        """Returns the selected log its ID."""
        return self.log["id"]

    @property
    def light(self):
        """Returns if the light was on in the room or not."""
        return self.log["light"]

    @property
    def time(self):
        """Returns the time in a datetime object."""
        t = loads(str(self.log["time"]).replace("'", '"'))
        return datetime(t["year"], t["month"], t["day"], t["hour"], t["minute"], t["second"], t["microsecond"])
