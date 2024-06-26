def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    sum = 0
    for i in range(len(lst)):
        if i % 2 != 0 and lst[i] % 2 == 0:
            sum += lst[i]
    return sum


# Test Cases
print(add([4, 2, 6, 7]))
print(add([1, 2, 3, 4, 5]))
print(add([1, 2, 3, 4, 5, 6]))
print(add([1, 2, 3, 4, 5, 6, 7]))
print(add([1, 2, 3, 4, 5, 6, 7, 8]))
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]))
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 2