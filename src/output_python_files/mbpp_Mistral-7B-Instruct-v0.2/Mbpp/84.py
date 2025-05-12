"""
Write a function to find the nth number in the newman conway sequence.
assert sequence(10) == 6
"""
def sequence(n):
    """
    :param n: int
    :return: int
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")

    a, b, c = 0, 1, 1
    for _ in range(n - 1):
        next_number = a + b
        a, b = b, next_number

    return next_number

if __name__ == "__main__":
    import unittest

    class TestSequence(unittest.TestCase):
        def test_sequence(self):
            self.assertEqual(sequence(1), 1)
            self.assertEqual(sequence(2), 1)
            self.assertEqual(sequence(3), 2)
            self.assertEqual(sequence(4), 2)
            self.assertEqual(sequence(5), 3)
            self.assertEqual(sequence(6), 3)
            self.assertEqual(sequence(7), 5)
            self.assertEqual(sequence(8), 5)
            self.assertEqual(sequence(9), 8)
            self.assertEqual(sequence(10), 6)
            self.assertEqual(sequence(11), 13)
            self.assertEqual(sequence(12), 13)
            self.assertEqual(sequence(13), 21)
            self.assertEqual(sequence(14), 21)
            self.assertEqual(sequence(15), 34)
            self.assertEqual(sequence(16), 34)
            self.assertEqual(sequence(17), 55)
            self.assertEqual(sequence(18), 55)
            self.assertEqual(sequence(19), 89)
            self.assertEqual(sequence(20), 89)
            self.assertEqual(sequence(21), 144)
            self.assertEqual(sequence(22), 144)
            self.assertEqual(sequence(23), 233)
            self.assertEqual(sequence(24), 233)
            self.assertEqual(sequence(25), 377)
            self.assertEqual(sequence(26), 377)
            self.assertEqual(sequence(27), 610)
            self.assertEqual(sequence(28), 610)
            self.assertEqual(sequence(29), 987)
            self.assertEqual(sequence(30), 987)
            self.assertEqual(sequence(31), 1597)
            self.assertEqual(sequence(32), 1597)
            self.assertEqual(sequence(33), 2584)
            self.assertEqual(sequence(34), 2584)
            self.assertEqual(sequence(35), 4181)
            self.assertEqual(sequence(36), 4181)
            self.assertEqual(sequence(37), 6765)
            self.assertEqual(sequence(38), 6765)
            self.assertEqual(sequence(39), 10946)
            self.assertEqual(sequence(40), 10946)
            self.assertEqual(sequence(41), 17711)
            self.assertEqual(sequence(42), 17711)
            self.assertEqual(sequence(43), 28657)
            self.assertEqual(sequence(44), 28657)
            self.assertEqual(sequence(45), 46368)
            self.assertEqual(sequence(46), 46368)
            self.assertEqual(sequence(47), 75025)
            self.assertEqual(sequence(48), 75025)
            self.assertEqual(sequence(49), 121393)
            self.assertEqual(sequence(50), 121393)
            self.assertEqual(sequence(51), 196418)
            self.assertEqual(sequence(5