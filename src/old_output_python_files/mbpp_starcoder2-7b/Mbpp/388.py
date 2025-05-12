"""
Write a python function to find the highest power of 2 that is less than or equal to n.
assert highest_Power_of_2(10) == 8
"""

def highest_Power_of_2(n):
    # TODO: Implement me
    return 0
<file_sep>/python/test/test_highest_power_of_2.py
import unittest
from highest_power_of_2 import highest_Power_of_2

class TestHighestPowerOf2(unittest.TestCase):
    def test_highest_power_of_2(self):
        self.assertEqual(highest_Power_of_2(10), 8)
        self.assertEqual(highest_Power_of_2(1), 1)
        self.assertEqual(highest_Power_of_2(2), 2)
        self.assertEqual(highest_Power_of_2(3), 2)
        self.assertEqual(highest_Power_of_2(4), 4)
        self.assertEqual(highest_Power_of_2(5), 4)
        self.assertEqual(highest_Power_of_2(6), 4)
        self.assertEqual(highest_Power_of_2(7), 4)
        self.assertEqual(highest_Power_of_2(8), 8)
        self.assertEqual(highest_Power_of_2(9), 8)
        self.assertEqual(highest_Power_of_2(10), 8)
        self.assertEqual(highest_Power_of_2(11), 8)
        self.assertEqual(highest_Power_of_2(12), 8)
        self.assertEqual(highest_Power_of_2(13), 8)
        self.assertEqual(highest_Power_of_2(14), 8)
        self.assertEqual(highest_Power_of_2(15), 8)
        self.assertEqual(highest_Power_of_2(16), 16)
        self.assertEqual(highest_Power_of_2(17), 16)
        self.assertEqual(highest_Power_of_2(18), 16)
        self.assertEqual(highest_Power_of_2(19), 16)
        self.assertEqual(highest_Power_of_2(20), 16)
        self.assertEqual(highest_Power_of_2(21), 16)
        self.assertEqual(highest_Power_of_2(22), 16)
        self.assertEqual(highest_Power_of_2(23), 16)
        self.assertEqual(highest_Power_of_2(24), 16)
        self.assertEqual(highest_Power_of_2(25), 16)
        self.assertEqual(highest_Power_of_2(26), 16)
        self.assertEqual(highest_Power_of_2(27), 16)
        self.assertEqual(highest_Power_of_2(28), 16)
        self.assertEqual(highest_Power_of_2(29), 16)
        self.assertEqual(highest_Power_of_2(30), 16)
        self.assertEqual(highest_Power_of_2(31), 16)
        self.assertEqual(highest_Power_of_2(32), 32)
        self.assertEqual(highest_Power_of_2(33), 32)
        self.assertEqual(highest_Power_of_2(34), 32)
        self.assertEqual(highest_Power_of_2(35), 32)
        self.assertEqual(highest_Power_of_2(36), 32)
        self.assertEqual(highest_Power_of_2(37), 32)
        self.assertEqual(highest_Power_of_2(38), 32)
        self.assertEqual(highest_Power_of_2(39), 32)
        self.assertEqual(highest_Power_of_2(40), 32)
        self.assertEqual(highest_Power_of_2(41), 32)
        self.assertEqual(highest_Power_of_2(42), 32)
        self.assertEqual(highest_Power_of_2(43), 32)
        self.assertEqual(highest_Power_of_2(44), 32)
        self.assertEqual(highest_Power_of_2(45), 32)