"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate(([1,2,3,4,5]))==False
"""
def test_duplicate(arr):
    """
    :param arr: list of integers
    :return: boolean
    """
    return len(arr) != len(set(arr))

if __name__ == "__main__":
    import unittest

    class TestDuplicate(unittest.TestCase):
        def test_duplicate(self):
            self.assertFalse(test_duplicate([1, 2, 3, 4, 5]))
            self.assertTrue(test_duplicate([1, 2, 2, 3, 4, 5]))
            self.assertTrue(test_duplicate([1, 1, 1, 1, 1, 1]))

    unittest.main()