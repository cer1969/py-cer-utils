# CRISTIAN ECHEVERRÍA RABÍ

from datetime import datetime, timedelta, tzinfo

#---------------------------------------------------------------------------------------------------
# Permite guardar con d.strftime(STR_FORMATO) y recuperar con datetime.strptime(txt, STR_FORMATO)

STR_FORMAT = "%Y-%m-%d %H:%M:%S.%f %z"

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

#---------------------------------------------------------------------------------------------------

def NT(txt_time):
    return datetime.strptime(txt_time, "%d-%m-%Y")


def fix_date(dt):
    """ Corrección de zona horaria para fechas en Chile"""
    if dt < NT("01-01-2006") or dt > NT("31-12-2016"):
        raise AttributeError("Rango de fecha no verificado")
    
    if NT("12-03-2006") <= dt < NT("08-10-2006"): return dt.replace(tzinfo=UTC_4)
    if NT("11-03-2007") <= dt < NT("14-10-2007"): return dt.replace(tzinfo=UTC_4)    
    if NT("30-03-2008") <= dt < NT("12-10-2008"): return dt.replace(tzinfo=UTC_4)
    if NT("08-03-2009") <= dt < NT("11-10-2009"): return dt.replace(tzinfo=UTC_4)
    if NT("04-04-2010") <= dt < NT("10-10-2010"): return dt.replace(tzinfo=UTC_4)
    if NT("08-05-2011") <= dt < NT("21-08-2011"): return dt.replace(tzinfo=UTC_4)
    if NT("29-04-2012") <= dt < NT("02-09-2012"): return dt.replace(tzinfo=UTC_4)
    if NT("28-04-2013") <= dt < NT("08-09-2013"): return dt.replace(tzinfo=UTC_4)
    if NT("27-04-2014") <= dt < NT("07-09-2014"): return dt.replace(tzinfo=UTC_4)
    if NT("15-05-2016") <= dt < NT("14-08-2016"): return dt.replace(tzinfo=UTC_4)
    
    return dt.replace(tzinfo=UTC_3)
