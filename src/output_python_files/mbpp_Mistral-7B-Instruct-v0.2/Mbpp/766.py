"""
Write a function to return a list of all pairs of consecutive items in a given list.
assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
"""
def pair_wise(input_list):
    """
    :param input_list: list
    :return: list of tuples
    """
    if len(input_list) < 2:
        return []
    return list(zip(input_list, input_list[1:]))

if __name__ == "__main__":
    import unittest

    class TestPairwise(unittest.TestCase):
        def test_pairwise(self):
            self.assertEqual(pair_wise([1, 1, 2, 3, 3, 4, 4, 5]), [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)])
            self.assertEqual(pair_wise([]), [])
            self.assertEqual(pair_wise([1]), [])
            self.assertEqual(pair_wise([1, 1]), [(1, 1)])
            self.assertEqual(pair_wise([1, 1, 1]), [(1, 1), (1, 1)])
            self.assertEqual(pair_wise([1, 1, 1, 1]), [(1, 1), (1, 1), (1, 1), (1, 1)])
            self.assertEqual(pair_wise([1, 1, 1, 1, 1]), [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1)])
            self.assertEqual(pair_wise([1, 1, 1, 1, 1, 1]), [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)])
            self.assertEqual(pair_wise([1, 1, 1, 1, 1, 1, 1]), [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)])
            self.assertEqual(pair_wise([1, 1, 1, 1, 1, 1, 1, 1]), [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)])
            self.assertEqual(pair_wise([1, 1, 1, 1, 1, 1, 1, 1, 1]), [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)])
            self.assertEqual(pair_wise([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)])
            self.assertEqual(pair_wise([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)])
            self.assertEqual(pair_wise([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1