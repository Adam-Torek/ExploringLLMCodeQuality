"""
Write a function to convert tuple string to integer tuple.
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
"""

def tuple_str_int(tup_str):
    tup_str = tup_str.strip("()")
    tup_list = tup_str.split(",")
    tup_list = [int(i.strip()) for i in tup_list]
    return tuple(tup_list)

# Test cases
print(tuple_str_int("(7, 8, 9)")) # Output: (7, 8, 9)
print(tuple_str_int("(1, 2, 3, 4, 5)")) # Output: (1, 2, 3, 4, 5)
print(tuple_str_int("(10, 20, 30, 40, 50)")) # Output: (10, 20, 30, 40, 50)
print(tuple_str_int("(100, 200, 300, 400, 500, 600)")) # Output: (100, 200, 300, 400, 500, 600)
print(tuple_str_int("(-1, 0, 1, 2, 3, 4, 5)")) # Output: (-1, 0, 1, 2, 3, 4, 5)
print(tuple_str_int("(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)")) # Output: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple_str_int("(-10, -20, -30, -40, -50, -60, -70, -80, -90)")) # Output: (-10, -20, -30, -40, -50, -60, -70, -80, -90)
print(tuple_str_int("(1000, -200, 300, -400, 500, -600, 700, -800, 900)")) # Output: (1000, -200, 300, -400, 500, -600, 700, -800, 900)
print(tuple_str_int("(10000, -2000, 3000, -4000, 5000, -6000, 7000, -8000, 9000)")) # Output: (1000, -200, 300, -400, 500, -600, 700, -800, 900)
print(tuple_str_int("(100000, -20000, 30000, -40000, 50000, -60000, 70000, -80000, 90000)")) # Output: (10000, -2000, 3000, -4000, 5000, -6000, 7000, -8000, 9000)
print(tuple_str_int("(1000000, -200000, 300000, -400000, 500000, -600000, 700000, -800000, 900000)")) # Output: (10000, -2000, 3000, -4000, 5000, -60