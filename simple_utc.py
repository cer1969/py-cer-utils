# CRISTIAN ECHEVERRÍA RABÍ

from datetime import datetime, timedelta, tzinfo

#---------------------------------------------------------------------------------------------------
# Permite guardar con d.strftime(STR_FORMATO) y recuperar con datetime.strptime(txt, STR_FORMATO)

def _get_current_utc_value():
    """Calcula diferencia horaria actual con UTC 0"""
    x = datetime.now()
    y = datetime.utcnow()
    x = x.replace(second=0, microsecond=0)
    y = y.replace(second=0, microsecond=0)
    return (x - y).total_seconds()/3600

STR_FORMAT = "%Y-%m-%d %H:%M:%S.%f %z"
CURRENT_UTC_VALUE = _get_current_utc_value()

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

UTC = SimpleUTC

#---------------------------------------------------------------------------------------------------

def replace(dt, tzvalue=CURRENT_UTC_VALUE):
    """ Devuelve dt reemplazando tzinfo de acuedo a tzvalue
        Al comparar dt con el resultado son distintos
    """
    return dt.replace(tzinfo=UTC(tzvalue))

def translate(dt, tzvalue=CURRENT_UTC_VALUE):
    """ Devuelve dt expresado en la zona dada por tzvalue
        Al comparar dt con el resultado son iguales
    """
    return dt.astimezone(UTC(tzvalue))

def to_str(dt):
    """ Devuelve dt como string con formato STR_FORMAT
        Si dt no tiene tzinfo se aplica CURRENT_UTC_VALUE
    """
    x = replace(dt) if dt.tzinfo is None else dt
    return x.strftime(STR_FORMAT)

def from_str(txt):
    """ Devuelve datetime object de acuerdo a formato STR_FORMAT
        txt debe incluir información de tzinfo
    """    
    return datetime.strptime(txt, STR_FORMAT)


#---------------------------------------------------------------------------------------------------

def NT(txt_time):
    return datetime.strptime(txt_time, "%d-%m-%Y")


def fix_date(dt):
    """ Corrección de zona horaria para fechas en Chile"""
    if dt < NT("01-01-2005") or dt > NT("13-05-2018"):
        raise AttributeError("Rango de fecha no verificado:" + to_str(dt))
    
    if NT("13-03-2005") <= dt < NT("09-10-2005"): return dt.replace(tzinfo=UTC(-4))
    if NT("12-03-2006") <= dt < NT("15-10-2006"): return dt.replace(tzinfo=UTC(-4))
    if NT("11-03-2007") <= dt < NT("14-10-2007"): return dt.replace(tzinfo=UTC(-4))    
    if NT("30-03-2008") <= dt < NT("12-10-2008"): return dt.replace(tzinfo=UTC(-4))
    if NT("08-03-2009") <= dt < NT("11-10-2009"): return dt.replace(tzinfo=UTC(-4))
    if NT("04-04-2010") <= dt < NT("10-10-2010"): return dt.replace(tzinfo=UTC(-4))
    if NT("08-05-2011") <= dt < NT("21-08-2011"): return dt.replace(tzinfo=UTC(-4))
    if NT("29-04-2012") <= dt < NT("02-09-2012"): return dt.replace(tzinfo=UTC(-4))
    if NT("28-04-2013") <= dt < NT("08-09-2013"): return dt.replace(tzinfo=UTC(-4))
    if NT("27-04-2014") <= dt < NT("07-09-2014"): return dt.replace(tzinfo=UTC(-4))
    if NT("15-05-2016") <= dt < NT("14-08-2016"): return dt.replace(tzinfo=UTC(-4))
    if NT("14-05-2017") <= dt < NT("13-08-2017"): return dt.replace(tzinfo=UTC(-4))
    
    return dt.replace(tzinfo=UTC(-3))
