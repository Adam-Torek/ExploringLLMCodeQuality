def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    """
    lst = [int(math.ceil(x))**2 for x in lst]
    return sum(lst)


# Test cases
print(sum_squares([1,2,3])) # should return 14
print(sum_squares([1,4,9])) # should return 98
print(sum_squares([1,3,5,7])) # should return 84
print(sum_squares([1.4,4.2,0])) # should return 29
print(sum_squares([-2.4,1,1])) # should return 6


# Test cases
assert sum_squares([1,2,3]) == 14
assert sum_squares([1,4,9]) == 98
assert sum_squares([1,3,5,7]) == 84
assert sum_squares([1.4,4.2,0]) == 29
assert sum_squares([-2.4,1,1]) == 6

# Test cases with negative numbers
assert sum_squares([-1,2,-3]) == 9
assert sum_squares([-1,4,-9]) == 98
assert sum_squares([-1,3,-5,-7]) == 84
assert sum_squares([-1.4,-4.2,0]) == 29
assert sum_squares([-2.4,-1,1]) == 6

# Test cases with decimals
assert sum_squares([1.5,2.6,3.1]) == 14
assert sum_squares([1.4,4.2,9.0]) == 98
assert sum_squares([1.3,5.5,7.7]) == 84
assert sum_squares([1.4,4.2,0.0]) == 29
assert sum_squares([-2.4,-1.0,1.0]) == 6

# Test cases with negative decimals
assert sum_squares([-1.5,-2.6,-3.1]) == 9
assert sum_squares([-1.4,-4.2,-9.0]) == 98
assert sum_squares([-1.3,-5.5,-7.7]) == 84
assert sum_squares([-1.4,-4.2,0.0]) == 29
assert sum_squares([-2.4,-1.0,-1.0]) == 6

# Test cases with negative numbers and decimals
assert sum_squares([-1.5,2.6,-3.1]) == 9
assert sum_squares([-1.4,4.2,-9.0]) == 98
assert sum_squares([-1.3,5.5,-7.7]) == 84
assert sum_squares([-1.4,4.2,0.0]) == 29
assert sum_squares([-2.4,-1.0,-1.0]) == 6

# Test cases with negative numbers and decimals
assert sum_squares([-1.5,2.6,-3.1]) == 9
assert sum_squares([-1.4,4.2,-9.0]) == 98
assert sum_squares([-1.3,5.5,-7.7]) == 84
assert sum_squares([-1.4,4.2,0.0]) == 29
assert sum_squares([-