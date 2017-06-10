# -*- coding: UTF-8 -*-

import unittest

from romme.parse import parse_date

class TestParse(unittest.TestCase):

    def test_parse_standard_date(self):
        for s in (
            "1 Vendémiaire, an I",
            "1 Vendémiaire I",
            "1er vendémiaire, I",
            "  1er vendemiaire,  i",
        ):
            self.assertEqual((1, 1, 1), parse_date(s), s)

    def test_parse_sansculottide_date(self):
        for s in (
            "jour de la vertu, an I",
            "jour de la vertu, I",
        ):
            self.assertEqual((1, 13, 1), parse_date(s), s)
