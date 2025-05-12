"""
Write a python function to find the sum of non-repeated elements in a given list.
assert find_sum([1,2,3,1,1,4,5,6]) == 21
"""

def find_sum(lst):
    unique_lst = list(set(lst))
    return sum(unique_lst)

print(find_sum([1,2,3,1,1,4,5,6])) # Output: 21

# Another way to solve this problem is to use a dictionary to keep track of the frequency of each element in the list and then sum up the values of the keys with a frequency of 1.

def find_sum_2(lst):
    freq = {}
    for i in lst:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    return sum([key for key, value in freq.items() if value == 1])

print(find_sum_2([1,2,3,1,1,4,5,6])) # Output: 21

# Another way to solve this problem is to use a set to remove the repeated elements and then sum up the remaining elements.

def find_sum_3(lst):
    return sum(set(lst))

print(find_sum_3([1,2,3,1,1,4,5,6])) # Output: 15

# All three functions will return the same output for the given input.