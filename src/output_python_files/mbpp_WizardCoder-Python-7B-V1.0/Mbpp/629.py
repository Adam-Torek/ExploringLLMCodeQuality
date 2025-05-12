"""
Write a python function to find even numbers from a list of numbers.
assert Split([1,2,3,4,5]) == [2,4]
"""

def Split(lst):
    even_lst = []
    for num in lst:
        if num % 2 == 0:
            even_lst.append(num)
    return even_lst

print(Split([1,2,3,4,5])) # Output: [2, 4]
print(Split([2,4,6,8,10])) # Output: [2, 4, 6, 8, 10]
print(Split([1,3,5,7,9])) # Output: []