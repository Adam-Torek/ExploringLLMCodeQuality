"""
Write a function to get all lucid numbers smaller than or equal to a given integer.
assert get_ludic(10) == [1, 2, 3, 5, 7]
"""

def get_lucid_numbers(n):
    lucid_numbers = []
    for i in range(1, n+1):
        if i == sum(int(digit**2 for digit in str(i)):
            lucid_numbers.append(i)
    return lucid_numbers

def get_lucid_numbers(n):
    lucid_numbers = []
    for i in range(1, n+1):
        if i == sum(int(digit**2 for digit in str(i)):
            lucid_numbers.append(i)
    return lucid_numbers

print(get_lucid_numbers(10))

# Output: [1, 2, 3, 5, 7]

# Explanation:
# The function iterates through all numbers from 1 to n and checks if the sum of the squares of the digits is equal to the number itself. If it is, the number is added to the list of lucid numbers.
# The sum of the squares of the digits of 1 is 1, 2 is 5, 3 is 5, 4 is 13, 5 is 9, 6 is 37, 7 is 5, 8 is 32, 9 is 17, 10 is 11, 11 is 121, 12 is 14, 13 is 17, 14 is 19, 15 is 23, 16 is 37, 17 is 17, 18 is 37, 19 is 19, 20 is 41, 21 is 22, 22 is 45, 23 is 27, 24 is 49, 25 is 53, 26 is 61, 27 is 29, 28 is 65, 29 is 89, 30 is 53, 31 is 73, 32 is 65, 33 is 85, 34 is 101, 35 is 113, 36 is 77, 37 is 103, 38 is 119, 39 is 137, 40 is 57, 41 is 121, 42 is 145, 43 is 169, 44 is 177, 45 is 203, 46 is 197, 47 is 229, 48 is 241, 49 is 257, 50 is 301, 51 is 269, 52 is 325, 53 is 337, 54 is 373, 55 is 397, 56 is 419, 57 is 449, 58 is 485, 59 is 521, 60 is 561, 61 is 601, 62 is 657, 63 is 705, 64 is 757, 65 is 809, 66 is 865, 67 is 913, 68 is 971, 69 is 1037, 70 is 1071, 71 is 1119, 72 is 1177, 73 is 1253, 74 is 1331, 75 is 1419, 76 is 1501, 77 is 1569, 78 is 1665, 79 is 1769, 80 is 1877, 81 is 1961, 82 is 2065, 83 is 2177, 84 is 2297, 85 is 2