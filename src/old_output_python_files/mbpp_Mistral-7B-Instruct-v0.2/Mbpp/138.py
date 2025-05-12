"""
Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.
assert is_Sum_Of_Powers_Of_Two(10) == True
"""
def is_Sum_Of_Powers_Of_Two(n):
    """
    :param n: int
    :return: bool
    """
    if n < 0:
        return False
    elif n == 0:
        return True
    elif (n & (n - 1)) == 0:
        return True
    else:
        for i in range(32):
            if (1 << i) & n:
                if (n - (1 << i)) % (1 << i) == 0:
                    n -= 1 << i
                    return is_Sum_Of_Powers_Of_Two(n)
        return False

if __name__ == "__main__":
    import unittest
    class TestIsSumOfPowersOfTwo(unittest.TestCase):
        def test_is_sum_of_powers_of_two(self):
            self.assertTrue(is_Sum_Of_Powers_Of_Two(10))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(-1))
            self.assertTrue(is_Sum_Of_Powers_Of_Two(0))
            self.assertTrue(is_Sum_Of_Powers_Of_Two(1))
            self.assertTrue(is_Sum_Of_Powers_Of_Two(5))
            self.assertTrue(is_Sum_Of_Powers_Of_Two(16))
            self.assertTrue(is_Sum_Of_Powers_Of_Two(25))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(2))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(3))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(4))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(6))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(7))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(8))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(9))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(11))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(12))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(13))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(14))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(15))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(20))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(21))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(22))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(23))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(24))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(25))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(26))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(27))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(28))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(29))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(30))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(31))
            self.assertFalse(is_Sum_Of_Powers_Of_Two(32))
            self.assertFalse