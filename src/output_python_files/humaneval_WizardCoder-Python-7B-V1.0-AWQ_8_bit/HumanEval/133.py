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
print(sum_squares([0,0,0])) # should return 0
print(sum_squares([1,2,3,4,5])) # should return 50
print(sum_squares([-1,-2,-3,-4])) # should return 36
print(sum_squares([1.5,2.5,3.5])) # should return 14
print(sum_squares([1.5,2.5,3.5,4.5])) # should return 14
print(sum_squares([1.5,2.5,3.5,4.5,5.5])) # should return 14
print(sum_squares([1.5,2.5,3.5,4.5,5.5,6.5])) # should return 14
print(sum_squares([1.5,2.5,3.5,4.5,5.5,6.5,7.5])) # should return 14
print(sum_squares([1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5])) # should return 14
print(sum_squares([1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5])) # should return 14
print(sum_squares([1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5])) # should return 14
print(sum_squares([1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5])) # should return 14
print(sum_squares([1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5])) # should return 14
print(sum_squares([1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5])) # should return 14
print(sum_squares([1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5,14.5])) # should return 14
print(sum_squares([1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,