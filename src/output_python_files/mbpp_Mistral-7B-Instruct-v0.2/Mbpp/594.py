"""
Write a function to find the difference of the first even and first odd number of a given list.
assert diff_even_odd([1,3,5,7,4,1,6,8])==3
"""
def diff_even_odd(numbers):
    """
    :param numbers: list of numbers
    :return: difference of the first even and first odd number
    """
    odd_number = None
    even_number = None
    for number in numbers:
        if even_number is None and number % 2 == 0:
            even_number = number
        elif odd_number is None and number % 2 != 0:
            odd_number = number
            break
    if odd_number is None or even_number is None:
        raise ValueError("List must contain at least one odd and one even number")
    return even_number - odd_number

if __name__ == "__main__":
    import unittest
    class TestDiffEvenOdd(unittest.TestCase):
        def test_diff_even_odd(self):
            self.assertEqual(diff_even_odd([1,3,5,7,4,1,6,8]), 3)
            self.assertEqual(diff_even_odd([2,3,5,7,4,1,6,8]), 4)
            self.assertEqual(diff_even_odd([1,2,3,4,5,6,7,8]), 3)
            self.assertEqual(diff_even_odd([1,2,3,4,5,6,7,9]), 3)
            self.assertEqual(diff_even_odd([1,2,3,4,5,6,7,8,9]), 4)
            self.assertEqual(diff_even_odd([1,2,3,4,5,6,7,8,9,10]), 5)
            self.assertEqual(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11]), 6)
            self.assertEqual(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12]), 7)
            self.assertEqual(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12,13]), 8)
            self.assertEqual(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14]), 9)
            self.assertEqual(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]), 10)
            self.assertEqual(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]), 11)
            self.assertEqual(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]), 12)
            self.assertEqual(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]), 13)
            self.assertEqual(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]), 14)
            self.assertEqual(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]), 15)
            self.assertEqual(diff_even_odd([1,2,3,4,5,6,7,8,9,10,11