"""
Write a function to find cubes of individual elements in a list.
assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
"""

def cube_nums(lst):
    return [num**3 for num in lst]

print(cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))<|endoftext|>