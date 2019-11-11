from unittest import TestCase

from util.partitions import partitions


class TestPartitions(TestCase):
    def test_partitions(self):
        parts = { 1 }
        self.assertEqual(partitions(parts, 1), 1)
