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

# Testing the function
print(add([4, 2, 6, 7])) # 2
print(add([1, 2, 3, 4, 5])) # 0
print(add([1, 2, 3, 4, 5, 6])) # 2
print(add([1, 2, 3, 4, 5, 6, 7])) # 2
print(add([1, 2, 3, 4, 5, 6, 7, 8])) # 2
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9])) # 4
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # 4
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) # 6
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) # 6
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) # 8
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) # 8
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) # 10
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])) # 10
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])) # 12
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])) # 12
print(add([1, 2, 3, 4, 5, 6, 7, 8