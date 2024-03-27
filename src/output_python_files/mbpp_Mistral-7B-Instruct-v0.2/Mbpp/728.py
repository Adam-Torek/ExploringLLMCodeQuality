"""
Write a function takes as input two lists [a_1,...,a_n], [b_1,...,b_n] and returns [a_1+b_1,...,a_n+b_n].
assert sum_list([10,20,30],[15,25,35])==[25,45,65]
"""
def sum_list(a,b):
    """
    Function takes as input two lists and returns the sum of each element in the lists
    """
    result = []
    for i in range(len(a)):
        result.append(a[i]+b[i])
    return result

# Test the function
assert sum_list([10,20,30],[15,25,35])==[25,45,65]</s>