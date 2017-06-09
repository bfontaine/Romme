# -*- coding: UTF-8 -*-

import jdcal


# These constants as well as the calculation in _ymd_to_jd below are based off
# PHP's FrenchToSdn in ext/calendar/french.c:
#   https://github.com/php/php-src/blob/6053987/ext/calendar/french.c
_DAYS_PER_4_YEARS = 1461
_FRENCH_JDN_OFFSET = 2375474

def _republican_ymd_to_julian_day(y, m, d):
    return (y * _DAYS_PER_4_YEARS) / 4 + (m-1) * 30 + d + _FRENCH_JDN_OFFSET

def republican_to_gregorian(y, m, d):
    """
    Take a year (y>=1), a month (1<=m<=13), and a day (1<=d<=30) that represent
    a day from the French Republican calendar and return a (year, month, day)
    tuple that represent the same date in the Gregorian calendar.
    """
    y, m, d, _ = jdcal.jd2gcal(0, _republican_ymd_to_julian_day(y, m, d))
    return (y, m, d)
