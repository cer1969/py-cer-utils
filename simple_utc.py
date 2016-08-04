# CRISTIAN ECHEVERRÍA RABÍ

from datetime import timedelta, tzinfo

#---------------------------------------------------------------------------------------------------

class SimpleUTC(tzinfo):
    def __init__(self, hours):
        self.__offset = timedelta(hours=hours)
        self.__name = "UTC%3d:00" % hours

    def utcoffset(self, dt):
        return self.__offset

    def tzname(self, dt):
        return self.__name

    def dst(self, dt):
        return timedelta(0)

UTC0 = SimpleUTC(0)
UTC_3 = SimpleUTC(-3)
UTC_4 = SimpleUTC(-4)