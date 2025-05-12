"""
Write a python function to remove odd numbers from a given list.
assert remove_odd([1,2,3]) == [2]
"""

def remove_odd(lst):
    return [num for num in lst if num % 2 == 0]

print(remove_odd([1,2,3])) # Output: [2]
print(remove_odd([1,3,5,4,6,8,9,0])) # Output: [4, 6, 0]
print(remove_odd([7,5,4,6,8,9,0])) # Output: [4, 6, 0]
print(remove_odd([1,3,5,7,9,9,2])) # Output: [2]
print(remove_odd([1,3,5,7,9,9,2,4,6,8])) # Output: [2, 4, 6]
print(remove_odd([1,3,5,7,9,9,2,4,6,8,10,12])) # Output: [2, 4, 6, 10]

# Another way to solve this problem using list comprehension
def remove_odd_list_comp(lst):
    return [num for num in lst if num % 2 != 0]

print(remove_odd_list_comp([1,2,3])) # Output: [2]
print(remove_odd_list_comp([1,3,5,4,6,8,9,0])) # Output: [4, 6, 0]
print(remove_odd_list_comp([1,3,5,7,9,9,2])) # Output: [2]
print(remove_odd_list_comp([1,3,5,7,9,9,2,4,6,8])) # Output: [2, 4, 6]
print(remove_odd_list_comp([1,3,5,7,9,9,2,4,6,8,10,12])) # Output: [2, 4, 6, 10]