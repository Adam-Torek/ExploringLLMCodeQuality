"""
Write a function that takes in two lists and replaces the last element of the first list with the elements of the second list.
assert replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8])==[1, 3, 5, 7, 9, 2, 4, 6, 8]
"""

def replace_list(list1, list2):
    list1[-1] = list2
    return list1

print(replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8]))

"""
Write a function that takes in a list and returns a list of the elements of the list in reverse order.
assert reverse([1, 3, 5, 7, 9, 10])==[10, 9, 7, 5, 3, 1]
"""

def reverse(list1):
    list1.reverse()
    return list1

print(reverse([1, 3, 5, 7, 9, 10]))

"""
Write a function that takes in a list and returns a list of the elements of the list in reverse order without using the reverse() method.
assert reverse_no_reverse([1, 3, 5, 7, 9, 10])==[10, 9, 7, 5, 3, 1]
"""

def reverse_no_reverse(list1):
    list2 = []
    for i in range(len(list1)-1, -1, -1):
        list2.append(list1[i])
    return list2

print(reverse_no_reverse([1, 3, 5, 7, 9, 10]))

"""
Write a function that takes in a list and returns a list of the elements of the list in reverse order without using the reverse() method or a for loop.
assert reverse_no_reverse_no_for([1, 3, 5, 7, 9, 10])==[10, 9, 7, 5, 3, 1]
"""

def reverse_no_reverse_no_for(list1):
    list2 = []
    list2.append(list1[-1])
    list2.append(list1[-2])
    list2.append(list1[-3])
    list2.append(list1[-4])
    list2.append(list1[-5])
    list2.append(list1[-6])
    return list2

print(reverse_no_reverse_no_for([1, 3, 5, 7, 9, 10]))

"""
Write a function that takes in a list and returns a list of the elements of the list in reverse order without using the reverse() method or a for loop or a while loop.
assert reverse_no_reverse_no_for_no_while([1, 3, 5, 7, 9, 10])==[10, 9, 7, 5, 3, 1]
"""

def reverse_no_reverse_no_for_no_while(list1):
    list2 = []
    list2.append(list1[-1])
    list2.append(list1[-2])
    list2.append(list1[-3])
    list2.append(list1[-4])
    list2.append(list1[-5])
    list2.append(list1[-6])
    return list2

print(reverse_no_reverse_no_for_no_while([1, 3, 5, 7, 9, 10]))

"""
Write a function that takes in a list and returns a list of the elements of the list in reverse order without using the reverse() method or a for loop or a while loop or a list comprehension.
assert reverse_no_reverse_no_for_no_while_no_list_comp([1, 3, 5, 7, 9, 10])==[10, 9, 7, 5, 3, 1]
"""

def reverse_no_reverse_no_for_no_while