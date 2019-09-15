from unittest import TestCase

from util.repeats import unit_fraction_cycle, repeats, tip_to_tail


class Test_repeats(TestCase):

    def test_repeats(self):
        self.assertEqual('', repeats('f'))
        self.assertEqual('f', repeats('ff'))
        self.assertEqual('flibbidy', repeats('flibbidyflibbidy'))
        self.assertEqual('flibbidy', repeats('jibbetflibbidyflibbidyf'))
        self.assertEqual('', repeats('jibbetflibbidyflib'))

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

    def test_tip_to_tail(self):
        self.assertTrue(tip_to_tail('abcabc', 'abc'))
        self.assertTrue(tip_to_tail('abcabca', 'abc'))
        self.assertTrue(tip_to_tail('dddabcabc', 'abc'))
        self.assertTrue(tip_to_tail('peqabcabca', 'abc'))
        self.assertFalse(tip_to_tail('peqabcabcp', 'abc'))
