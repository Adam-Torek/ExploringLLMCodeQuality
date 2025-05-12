"""
Write a function to find the product of first even and odd number of a given list.
assert mul_even_odd([1,3,5,7,4,1,6,8])==4
"""
def mul_even_odd(numbers):
    """
    :param numbers: list of numbers
    :return: product of first even and odd number
    """
    even_number = None
    odd_number = None
    for number in numbers:
        if even_number is None and number % 2 == 0:
            even_number = number
        elif odd_number is None and number % 2 != 0:
            odd_number = number
            break
    if even_number is None or odd_number is None:
        raise ValueError("List should contain at least one even and one odd number")
    return even_number * odd_number

if __name__ == "__main__":
    import unittest
    class TestMulEvenOdd(unittest.TestCase):
        def test_mul_even_odd(self):
            self.assertEqual(mul_even_odd([1,3,5,7,4,1,6,8]), 4)
            self.assertEqual(mul_even_odd([2,3,5,7,4,1,6,8]), 12)
            self.assertEqual(mul_even_odd([1,2,3,4,5,6,7,8]), 12)
            self.assertEqual(mul_even_odd([1,2,3,4,5,6,7,9]), 12)
            self.assertEqual(mul_even_odd([1,2,3,4,5,6,7,10]), 12)
            self.assertEqual(mul_even_odd([1,2,3,4,5,6,7,11]), ValueError)
            self.assertEqual(mul_even_odd([1,2,3,4,5,6,7,12]), 48)
            self.assertEqual(mul_even_odd([1,2,3,4,5,6,7,13]), ValueError)
            self.assertEqual(mul_even_odd([1,2,3,4,5,6,7,14]), 28)
            self.assertEqual(mul_even_odd([1,2,3,4,5,6,7,15]), ValueError)
            self.assertEqual(mul_even_odd([1,2,3,4,5,6,7,16]), 64)
            self.assertEqual(mul_even_odd([1,2,3,4,5,6,7,17]), ValueError)
            self.assertEqual(mul_even_odd([1,2,3,4,5,6,7,18]), 72)
            self.assertEqual(mul_even_odd([1,2,3,4,5,6,7,19]), ValueError)
            self.assertEqual(mul_even_odd([1,2,3,4,5,6,7,20]), 120)
            self.assertEqual(mul_even_odd([1,2,3,4,5,6,7,21]), ValueError)
            self.assertEqual(mul_even_odd([1,2,3,4,5,6,7,22]), 132)
            self.assertEqual(mul_even_odd([1,2,3,4,5,6,7,23]), ValueError)
            self.assertEqual(mul_even_odd([1,2,3,4,5,6,7,24]), 288)
            self.assertEqual(mul_even_odd([1,2,3,4,5,6,7,25]), ValueError)
            self.assertEqual(mul_even_odd([1,2,3,4,5,6,7,26]), 324)
            self.assertEqual(mul_even_odd([1,2,3,4,5,6,7,27]), ValueError)
            self.assertEqual(mul_even_odd([1,2,3,4,5,6,7,28]), 512)
            self.assertEqual(mul_even_odd([1,2,3,4,5,6,7,29]), ValueError)
            self.assertEqual(mul