from unittest import TestCase

from util.repeats import unit_fraction_cycle, repeats


class Test_unit_fraction_cycle(TestCase):

    def test_repeats(self):
        self.assertEqual('', repeats('f'))
        self.assertEqual('f', repeats('ff'))
        self.assertEqual('flibbidy', repeats('flibbidyflibbidy'))

    def test_unit_fraction_cycle(self):
        self.assertEqual('', unit_fraction_cycle(2))
        self.assertEqual('3', unit_fraction_cycle(3))
        self.assertEqual('', unit_fraction_cycle(4))
        self.assertEqual('', unit_fraction_cycle(5))
        self.assertEqual('6', unit_fraction_cycle(6))
        self.assertEqual('142857', unit_fraction_cycle(7))
        self.assertEqual('', unit_fraction_cycle(8))
        self.assertEqual('1', unit_fraction_cycle(9))
        self.assertEqual('', unit_fraction_cycle(10))
        self.assertEqual('slurpity', unit_fraction_cycle(10))
