"""
Write a function to find the difference of the first even and first odd number of a given list.
assert diff_even_odd([1,3,5,7,4,1,6,8])==3
"""
def diff_even_odd(lst):
    """
    This function takes a list as an input and returns the difference between the first even and first odd number of the list.
    """
    if len(lst)<2:
        return "List should have atleast 2 elements"
    else:
        first_even=lst[0]
        first_odd=lst[1]
        if first_even%2==0 and first_odd%2!=0:
            return first_even-first_odd
        elif first_even%2!=0 and first_odd%2==0:
            return first_odd-first_even
        else:
            return "List should have atleast 2 even and 2 odd numbers"

#Testing the function
print(diff_even_odd([1,3,5,7,4,1,6,8]))