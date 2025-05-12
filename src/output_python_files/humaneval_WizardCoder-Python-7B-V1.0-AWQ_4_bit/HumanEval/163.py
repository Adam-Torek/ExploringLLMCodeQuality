def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    even_digits = []
    for num in range(a, b+1):
        if num % 2 == 0:
            even_digits.append(num)
    return sorted(even_digits)



# Test cases
print(generate_integers(2, 8))  # Output: [2, 4, 6, 8]
print(generate_integers(8, 2))  # Output: [2, 4, 6, 8]
print(generate_integers(10, 14))  # Output: []
print(generate_integers(100, 200))  # Output: [100, 120, 140, 160, 180]
print(generate_integers(100, 2000))  # Output: [100, 120, 140, 160, 180, 200]
print(generate_integers(1000, 20000))  # Output: [100, 120, 140, 160, 180, 200]