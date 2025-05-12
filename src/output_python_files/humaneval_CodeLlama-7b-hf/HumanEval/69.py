def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    # TODO: Implement me
    pass


# ## Unit Test
# 
# 
# 
# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_search.py
import unittest


class TestSearch(unittest.TestCase):

    def test_search(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)
        self.assertEqual(search([1, 2, 3, 4, 5]), 1)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 1)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), 1)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), 1)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), 1)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 1)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), 1)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), 1)
        self.assertEqual(search