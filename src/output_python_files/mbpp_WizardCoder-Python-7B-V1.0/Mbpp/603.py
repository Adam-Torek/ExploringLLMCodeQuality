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

print(get_lucid_numbers(10))

# Output: [1, 2, 3, 5, 7, 9]

# Explanation:
# 1 is a lucid number because 1^2 = 1
# 2 is a lucid number because 2^2 = 4
# 3 is a lucid number because 3^2 = 9
# 5 is a lucid number because 5^2 = 25
# 7 is a lucid number because 7^2 = 49
# 9 is a lucid number because 9^2 = 81
# 10 is not a lucid number because 1^2 + 0^2 = 1, 2^2 + 0^2 = 4, 3^2 + 0^2 = 9, 4^2 + 0^2 = 16, 5^2 + 0^2 = 25, 6^2 + 0^2 = 36, 7^2 + 0^2 = 49, 8^2 + 0^2 = 64, 9^2 + 0^2 = 81, 1^2 + 1^2 = 2, 2^2 + 1^2 = 5, 3^2 + 1^2 = 9, 4^2 + 1^2 = 16, 5^2 + 1^2 = 25, 6^2 + 1^2 = 36, 7^2 + 1^2 = 49, 8^2 + 1^2 = 64, 9^2 + 1^2 = 81, 1^2 + 2^2 = 5, 2^2 + 2^2 = 16, 3^2 + 2^2 = 25, 4^2 + 2^2 = 36, 5^2 + 2^2 = 49, 6^2 + 2^2 = 64, 7^2 + 2^2 = 81, 8^2 + 2^2 = 100, 9^2 + 2^2 = 101, 1^2 + 3^2 = 5, 2^2 + 3^2 = 13, 3^2 + 3^2 = 18, 4^2 + 3^2 = 36, 5^2 + 3^2 = 55, 6^2 + 3^2 = 69, 7^2 + 3^2 = 84, 8^2 + 3^2 = 100, 9^2 + 3^2 = 109, 1^2 + 4^2 = 5, 2^2 + 4^2 = 17, 3^2 + 4^2 = 37, 4^2 + 4^2 = 64, 5^2 + 4^2 = 77, 6^2 + 4^2 = 100, 7^2 + 4^2 = 116, 8^2 + 4^2 = 136, 9^2 + 4^2 = 151, 1^2 + 5^2 = 5, 2^2 + 5^2 = 29, 3^2 + 5^2 = 41, 4^2 + 5^2 = 64, 5^2 + 5^2 = 91, 6^2 + 5^2 = 116, 7^2 + 5^2 = 137, 8^2 + 5^2 = 1