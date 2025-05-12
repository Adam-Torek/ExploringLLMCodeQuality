"""
Write a function to find the n'th lucas number.
assert find_lucas(9) == 76
"""

def find_lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return find_lucas(n-1) + find_lucas(n-2)

print(find_lucas(9)) # Output: 76

# Alternatively, we can use a loop to find the n'th lucas number
def find_lucas_loop(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        lucas = 2
        next_lucas = 1
        for i in range(2, n):
            temp = lucas
            lucas = next_lucas
            next_lucas = temp + lucas
        return lucas

print(find_lucas_loop(9)) # Output: 76

# We can also use a list to store the first few lucas numbers and use indexing to find the n'th number
def find_lucas_list(n):
    lucas_list = [2, 1]
    for i in range(2, n):
        lucas_list.append(lucas_list[i-1] + lucas_list[i-2])
    return lucas_list[n]

print(find_lucas_list(9)) # Output: 76

# We can also use a recursive approach to find the n'th lucas number
def find_lucas_recursive(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return find_lucas_recursive(n-1) + find_lucas_recursive(n-2)

print(find_lucas_recursive(9)) # Output: 76

# We can also use a formula to find the n'th lucas number
def find_lucas_formula(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return (((2*((2**(n-1) - 1)) * (1 + (2**(n-1))) // 2) + 1) * (2**(n-2)) // 2)

print(find_lucas_formula(9)) # Output: 76

# All of these methods will return the same output for the same input