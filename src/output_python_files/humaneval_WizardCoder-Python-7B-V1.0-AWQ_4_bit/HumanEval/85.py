def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return sum(lst[1::2])


# Test cases
print(add([4, 2, 6, 7]))  # Output: 2
print(add([1, 3, 5, 8, 4, 6, 7, 9, 2]))  # Output: 12
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: 0
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output: 20
print(add([1, 3, 5, 7, 9, 11, 13, 15]))  # Output: 0
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))  # Output: 30
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))  # Output: 30
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))  # Output: 30
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))  # Output: 30
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))  # Output: 30
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))  # Output: 30
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]))  # Output: 30
print(add([1, 2, 3, 4, 5, 6, 7, 8,