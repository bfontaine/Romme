# -*- coding: UTF-8 -*-

import unittest

from romme.dates import RepublicanDate

class TestDates(unittest.TestCase):

    def test_str(self):
        rd = RepublicanDate(1, 1, 1)
        self.assertEqual("1 Vendémiaire, an I", str(rd))
