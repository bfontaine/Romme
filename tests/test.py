# -*- coding: UTF-8 -*-
import sys
import random
import argparse
import unittest

from os.path import dirname

if __name__ == '__main__':
    here = dirname(__file__)
    sys.path.insert(0, here+'/..')

import romme

class TestRommeVersion(unittest.TestCase):
    def test_version(self):
        self.assertRegexpMatches(romme.__version__, r'^\d+\.\d+\.\d+')

if __name__ == '__main__':
    # Use an explicit random seed so one can reproduce the tests
    p = argparse.ArgumentParser()
    p.add_argument("--seed", type=int, help="Force the random seed")
    opts = p.parse_args()

    seed = opts.seed or int(random.random() * 1000)
    print("Random seed: %d" % seed)
    random.seed(seed)

    suite = unittest.defaultTestLoader.discover(here)
    t = unittest.TextTestRunner().run(suite)
    if not t.wasSuccessful():
        sys.exit(1)
