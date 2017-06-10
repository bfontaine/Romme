# -*- coding: UTF-8 -*-

import unittest

from romme.romans import roman_to_decimal, decimal_to_roman

_tests = (
    (1, "I"),
    (2, "II"),
    (5, "V"),
    (9, "IX"),
    (12, "XII"),
    (98, "XCVIII"),
    (99, "XCIX"),
    (2000, "MM"),
)

class TestRomans(unittest.TestCase):

    def test_roman_to_decimal(self):
        for decimal, roman in _tests:
            self.assertEqual(decimal, roman_to_decimal(roman))
            self.assertEqual(decimal, roman_to_decimal(roman.lower()))

    def test_decimal_to_roman(self):
        for decimal, roman in _tests:
            self.assertEqual(roman, decimal_to_roman(decimal))
