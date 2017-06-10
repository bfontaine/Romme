# -*- coding: UTF-8 -*-

import unittest

from romme import conversion as conv

republican_leap_years = {3, 7, 11}

# Let's do exhaustive tests because they aren't so many dates
def all_dates():
    for y in range(1, 14+1):
        for m in range(1, 13+1):
            max_days = 30
            if m == 13:
                max_days = 6 if y in republican_leap_years else 5
            for d in range(1, max_days+1):
                yield (y, m, d)

class TestConvertion(unittest.TestCase):

    def test_all_julian_republican(self):
        for y, m, d in all_dates():
            jd = conv._republican_ymd_to_julian_day(y, m, d)
            self.assertEqual((y, m, d),
                    conv._julian_day_to_republican_ymd(jd))

    def test_gregorian_to_republican(self):
        # see https://fr.wikipedia.org/wiki/An_I_du_calendrier_r%C3%A9publicain
        # for examples
        self.assertEqual((1, 1, 1),
                conv.gregorian_to_republican(1792, 9, 22))
        self.assertEqual((1, 12, 30),
                conv.gregorian_to_republican(1793, 9, 16))
        self.assertEqual((4, 1, 1),
                conv.gregorian_to_republican(1795, 9, 23))

    def test_republican_to_gregorian(self):
        self.assertEqual((1792, 9, 22),
                conv.republican_to_gregorian(1, 1, 1))
        self.assertEqual((1793, 9, 16),
                conv.republican_to_gregorian(1, 12, 30))
        self.assertEqual((1795, 9, 23),
                conv.republican_to_gregorian(4, 1, 1))

    def test_all_republican_gregorian(self):
        for rep in all_dates():
            greg = conv.republican_to_gregorian(*rep)
            rep2 = conv.gregorian_to_republican(*greg)

            self.assertEqual(rep, rep2, "%d-%d-%d" % greg)
