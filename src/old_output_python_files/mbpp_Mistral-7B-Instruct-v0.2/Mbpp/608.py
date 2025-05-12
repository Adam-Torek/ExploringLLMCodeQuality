"""
Write a python function to find nth bell number.
assert bell_Number(2) == 2
"""
def bell_Number(n):
    if n < 0:
        raise ValueError("n must be non-negative integer")

    bell = [0] * (n + 1)
    bell[0] = 1

    for i in range(1, n + 1):
        bell[i] = sum(bell[i - 1:])

    return bell[n]

if __name__ == "__main__":
    import unittest

    class TestBellNumber(unittest.TestCase):
        def test_bell_number(self):
            self.assertEqual(bell_Number(2), 2)
            self.assertEqual(bell_Number(3), 3)
            self.assertEqual(bell_Number(4), 10)
            self.assertEqual(bell_Number(5), 25)
            self.assertEqual(bell_Number(6), 61)
            self.assertEqual(bell_Number(7), 171)
            self.assertEqual(bell_Number(8), 484)
            self.assertEqual(bell_Number(9), 1405)
            self.assertEqual(bell_Number(10), 4291)
            self.assertEqual(bell_Number(11), 13953)
            self.assertEqual(bell_Number(12), 46368)
            self.assertEqual(bell_Number(13), 154701)
            self.assertEqual(bell_Number(14), 514835)
            self.assertEqual(bell_Number(15), 1771073)
            self.assertEqual(bell_Number(16), 6065155)
            self.assertEqual(bell_Number(17), 20358008)
            self.assertEqual(bell_Number(18), 68719476)
            self.assertEqual(bell_Number(19), 237582561)
            self.assertEqual(bell_Number(20), 806515533)
            self.assertEqual(bell_Number(21), 2799336673)
            self.assertEqual(bell_Number(22), 9876513301)
            self.assertEqual(bell_Number(23), 34164546229)
            self.assertEqual(bell_Number(24), 119750456189)
            self.assertEqual(bell_Number(25), 416129729601)
            self.assertEqual(bell_Number(26), 1451375203521)
            self.assertEqual(bell_Number(27), 5084585466186)
            self.assertEqual(bell_Number(28), 18363119030930)
            self.assertEqual(bell_Number(29), 65231669609234)
            self.assertEqual(bell_Number(30), 232131405343601)

    unittest.main()