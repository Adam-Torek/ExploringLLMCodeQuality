"""
Write a function to find cubes of individual elements in a list.
assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
"""

def cube_nums(lst):
    return [x**3 for x in lst]

print(cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Output: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# Test cases:
# assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
# assert cube_nums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])==[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
# assert cube_nums([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
# assert cube_nums([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])==[1000, 729, 512, 343, 216, 125, 8, 27, 1]
# assert cube_nums([1])==[1]
# assert cube_nums([])==[]
# assert cube_nums([-1])==[1]
# assert cube_nums([0])==[0]
# assert cube_nums([2.5, 3.5, 4.5])==[]
# assert cube_nums("abc")==[]
# assert cube_nums([1, 2, 3, "a", 4, 5, 6])==[1, 8, 27, 64, 125, 216, 343, 512, 729]
# assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 144]
# assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 144, 216]
# assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 144, 216, 343]
# assert cube_nums([1,