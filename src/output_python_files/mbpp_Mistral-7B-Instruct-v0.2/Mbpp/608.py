"""
Write a python function to find nth bell number.
assert bell_Number(2) == 2
"""
def bell_Number(n):
    if n < 0:
        raise ValueError("n must be non-negative integer")

    bell = [1] * (n + 1)
    for i in range(1, n + 1):
        bell[i] = sum(bell[i - 1:])

    return bell[n]

if __name__ == "__main__":
    import unittest

    class TestBellNumber(unittest.TestCase):
        def test_bell_number(self):
            self.assertEqual(bell_Number(2), 2)
            self.assertEqual(bell_Number(3), 5)
            self.assertEqual(bell_Number(4), 15)
            self.assertEqual(bell_Number(5), 35)
            self.assertEqual(bell_Number(10), 211)

    unittest.main()