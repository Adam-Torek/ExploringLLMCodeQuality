"""
Write a function to find the n'th star number.
assert find_star_num(3) == 37
"""
def find_star_num(n):
    """
    Find the n'th star number.
    """
    star_num = 0
    for i in range(1, n+1):
        star_num += i*(i+1)//2
    return star_num

if __name__ == "__main__":
    import unittest
    class TestFindStarNum(unittest.TestCase):
        def test_find_star_num(self):
            self.assertEqual(find_star_num(3), 37)
            self.assertEqual(find_star_num(10), 171)
            self.assertEqual(find_star_num(1), 1)
            self.assertEqual(find_star_num(0), 0)
    unittest.main()</s>