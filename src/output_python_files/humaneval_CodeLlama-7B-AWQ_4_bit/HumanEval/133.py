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
    lst = [int(math.ceil(x)) for x in lst]
    return sum([x**2 for x in lst])


if __name__ == '__main__':
    print("Example:")
    print(sum_squares([1, 2, 3]))

    #These "asserts" using only for self-checking and not necessary for
    #auto-testing
    assert sum_squares([1, 2, 3]) == 14, "First"
    assert sum_squares([1, 4, 9]) == 98, "Second"
    assert sum_squares([1, 3, 5, 7]) == 84, "Third"
    assert sum_squares([1.4, 4.2, 0]) == 29, "Fourth"
    assert sum_squares([-2.4, 1, 1]) == 6, "Fifth"
    print("Coding complete? Click 'Check' to earn cool rewards!")