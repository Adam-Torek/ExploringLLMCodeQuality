"""
Write a function to find squares of individual elements in a list.
assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

def square_nums(lst):
    return [x**2 for x in lst]

print(square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Test cases:
# assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# assert square_nums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])==[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# assert square_nums([-1, -2, -3, -4, -5, -6, -7, -8, -9])==[1, 4, 9, 16, 25, 36, 49, 64, 81]
# assert square_nums([10, 9, 8, 7, 6, 5, 4, 3, 2])==[100, 81, 64, 49, 36, 25, 16, 9, 4]
# assert square_nums([0, 0, 0, 0, 0, 0, 0, 0, 0])==[0, 0, 0, 0, 0, 0, 0, 0, 0]
# assert square_nums([1])==[1]
# assert square_nums([])==[]
# assert square_nums([-1, 0, 1])==[1, 0, 1]
# assert square_nums([-1, 0, 1, -2, 3, -4, 5])==[1, 0, 1, 4, 9, 16, 25]
# assert square_nums([1.5, 2.3, 3.14, 4.2])==[1.5, 2.3, 3.14, 4.2]
# assert square_nums([])==[]
# assert square_nums([1, 2, 3, "a", "b", "c"])==[1, 4, 9, "a", "b", "c"]
# assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 111]
# assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
# assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])==[1, 4, 9, 16, 25, 36, 49, 64,