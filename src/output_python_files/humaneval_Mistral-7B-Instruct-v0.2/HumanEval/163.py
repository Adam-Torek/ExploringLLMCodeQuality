def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Your code here
    result = []
    while a <= b:
        if a % 2 == 0:
            result.append(a)
        a += 1
    return result

# Test cases
print(generate_integers(2, 8))
print(generate_integers(8, 2))
print(generate_integers(10, 14))
print(generate_integers(1, 1))
print(generate_integers(100, 100))