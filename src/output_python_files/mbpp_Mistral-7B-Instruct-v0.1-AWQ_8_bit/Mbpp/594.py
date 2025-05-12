"""
Write a function to find the difference of the first even and first odd number of a given list.
assert diff_even_odd([1,3,5,7,4,1,6,8])==3
"""
def diff_even_odd(lst):
    """
    This function takes a list as an input and returns the difference between the first even and first odd number of the list.
    """
    if len(lst)<2:
        return None
    else:
        first_even=lst[0]
        first_odd=lst[1]
        if first_even%2==0 and first_odd%2!=0:
            return first_odd-first_even
        elif first_even%2!=0 and first_odd%2==0:
            return first_even-first_odd
        else:
            return None

# Test the function
assert diff_even_odd([1,3,5,7,4,1,6,8])==3
assert diff_even_odd([1,2,3,4,5,6,7,8])==1
assert diff_even_odd([1,2,3,4,5,6,7,8,9])==None