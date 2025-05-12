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

def get_ludic(n):
    lucid_numbers = get_lucid_numbers(n)
    return [i for i in range(1, n+1) if i in lucid_numbers]

print(get_ludic(10)) # [1, 2, 3, 5, 7]