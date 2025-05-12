"""
Write a function takes as input two lists [a_1,...,a_n], [b_1,...,b_n] and returns [a_1+b_1,...,a_n+b_n].
assert sum_list([10,20,30],[15,25,35])==[25,45,65]
"""
def sum_list(list1,list2):
    return [list1[i]+list2[i] for i in range(len(list1))]

print(sum_list([10,20,30],[15,25,35]))

"""
Write a function takes as input two lists [a_1,...,a_n], [b_1,...,b_n] and returns [a_1*b_1,...,a_n*b_n].
assert multiply_list([10,20,30],[15,25,35])==[150,500,1050]
"""
def multiply_list(list1,list2):
    return [list1[i]*list2[i] for i in range(len(list1))]

print(multiply_list([10,20,30],[15,25,35]))

"""
Write a function takes as input two lists [a_1,...,a_n], [b_1,...,b_n] and returns [a_1/b_1,...,a_n/b_n].
assert divide_list([10,20,30],[15,25,35])==[0.6666666666666666,0.8,0.8666666666666667]
"""
def divide_list(list1,list2):
    return [list1[i]/list2[i] for i in range(len(list1))]

print(divide_list([10,20,30],[15,25,35]))

"""
Write a function takes as input two lists [a_1,...,a_n], [b_1,...,b_n] and returns [a_1-b_1,...,a_n-b_n].
assert subtract_list([10,20,30],[15,25,35])==[-5,-5,-5]
"""
def subtract_list(list1,list2):
    return [list1[i]-list2[i] for i in range(len(list1))]

print(subtract_list([10,20,30],[15,25,35]))

"""
Write a function takes as input two lists [a_1,...,a_n], [b_1,...,b_n] and returns [a_1**b_1,...,a_n**b_n].
assert power_list([10,20,30],[15,25,35])==[100000000000000000000, 655360000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000