"""
Write a function to subtract two lists element-wise.
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
"""
def sub_list(list1,list2):
    return [list1[i]-list2[i] for i in range(len(list1))]

print(sub_list([1, 2, 3],[4,5,6]))

"""
Write a function to find the maximum of two lists element-wise.
assert max_list([1, 2, 3],[4,5,6])==[4,5,6]
"""
def max_list(list1,list2):
    return [max(list1[i],list2[i]) for i in range(len(list1))]

print(max_list([1, 2, 3],[4,5,6]))

"""
Write a function to find the minimum of two lists element-wise.
assert min_list([1, 2, 3],[4,5,6])==[1,2,3]
"""
def min_list(list1,list2):
    return [min(list1[i],list2[i]) for i in range(len(list1))]

print(min_list([1, 2, 3],[4,5,6]))

"""
Write a function to find the average of two lists element-wise.
assert avg_list([1, 2, 3],[4,5,6])==[2.5,3.5,4.5]
"""
def avg_list(list1,list2):
    return [(list1[i]+list2[i])/2 for i in range(len(list1))]

print(avg_list([1, 2, 3],[4,5,6]))

"""
Write a function to find the dot product of two lists.
assert dot_list([1, 2, 3],[4,5,6])==32
"""
def dot_list(list1,list2):
    return sum([list1[i]*list2[i] for i in range(len(list1))])

print(dot_list([1, 2, 3],[4,5,6]))

"""
Write a function to find the sum of two lists element-wise.
assert sum_list([1, 2, 3],[4,5,6])==[5,7,9]
"""
def sum_list(list1,list2):
    return [list1[i]+list2[i] for i in range(len(list1))]

print(sum_list([1, 2, 3],[4,5,6]))

"""
Write a function to find the product of two lists element-wise.
assert prod_list([1, 2, 3],[4,5,6])==[4,10,18]
"""
def prod_list(list1,list2):
    return [list1[i]*list2[i] for i in range(len(list1))]

print(prod_list([1, 2, 3],[4,5,6]))

"""
Write a function to find the square of two lists element-wise.
assert square_list([1, 2, 3],[4,5,6])==[1,4,9]
"""
def square_list(list1,list2):
    return [list1[i]**2 for i in range(len(list1))]

print(square_list([1, 2, 3],[4,5,6]))

"""
Write a function to find the square root of two lists element-wise.
assert sqrt_list([1, 2, 3],[4,5,6])==[1,2,3]
"""
def sqrt_list(list1,list2):
    return [list1[i]**0.5 for i in range(len(list1))]

print(sqrt_list([1, 2, 3],[4,5,6]))

"""
Write a function to find the power of two lists element-wise.
assert pow_list([1, 2, 3],[4,5,6])==[1,32,729]
"""
def pow_list(list1,list2):
    return [list1[i]**list2[i] for i in range(