"""
Write a function takes as input two lists [a_1,...,a_n], [b_1,...,b_n] and returns [a_1+b_1,...,a_n+b_n].
assert sum_list([10,20,30],[15,25,35])==[25,45,65]
"""
def sum_list(a,b):
    return [a[i]+b[i] for i in range(len(a))]

"""
Write a function takes as input a list of numbers and returns the sum of the numbers.
assert sum_list([10,20,30])==60
"""
def sum_list(a):
    return sum(a)

"""
Write a function takes as input a list of numbers and returns the average of the numbers.
assert average_list([10,20,30])==20
"""
def average_list(a):
    return sum(a)/len(a)

"""
Write a function takes as input a list of numbers and returns the largest number in the list.
assert max_list([10,20,30])==30
"""
def max_list(a):
    return max(a)

"""
Write a function takes as input a list of numbers and returns the smallest number in the list.
assert min_list([10,20,30])==10
"""
def min_list(a):
    return min(a)

"""
Write a function takes as input a list of numbers and returns the number of elements in the list.
assert len_list([10,20,30])==3
"""
def len_list(a):
    return len(a)

"""
Write a function takes as input a list of numbers and returns the number of even elements in the list.
assert even_count([10,20,30])==2
"""
def even_count(a):
    return len([i for i in a if i%2==0])

"""
Write a function takes as input a list of numbers and returns the number of odd elements in the list.
assert odd_count([10,20,30])==1
"""
def odd_count(a):
    return len([i for i in a if i%2==1])

"""
Write a function takes as input a list of numbers and returns the number of positive elements in the list.
assert positive_count([10,-20,30])==2
"""
def positive_count(a):
    return len([i for i in a if i>0])

"""
Write a function takes as input a list of numbers and returns the number of negative elements in the list.
assert negative_count([10,-20,30])==1
"""
def negative_count(a):
    return len([i for i in a if i<0])

"""
Write a function takes as input a list of numbers and returns the number of zeroes in the list.
assert zero_count([10,-20,30])==0
"""
def zero_count(a):
    return len([i for i in a if i==0])

"""
Write a function takes as input a list of numbers and returns the number of elements that are divisible by 3.
assert divisible_by_3_count([10,20,30])==1
"""
def divisible_by_3_count(a):
    return len([i for i in a if i%3==0])

"""
Write a function takes as input a list of numbers and returns the number of elements that are divisible by 5.
assert divisible_by_5_count([10,20,30])==2
"""
def divisible_by_5_count(a):
    return len([i for i in a if i%5==0])

"""
Write a function takes as input a list of numbers and returns the number of elements that are divisible by 7.
assert divisible_by_7_count([10,20,30])==0
"""
def divisible_by_7_count(a):
    return len([i for i in a if i%7==0])

"""
Write a function takes as input a list of numbers and returns the number of elements that are divisible by 1