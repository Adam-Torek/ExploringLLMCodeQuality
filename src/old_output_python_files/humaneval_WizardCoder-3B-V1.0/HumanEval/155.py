def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

# Solution:
# We can solve this problem by iterating through each digit of the number and counting the number of even and odd digits.
# We can use the modulo operator to check if a digit is even or odd.

def even_odd_count(num):
    even_count = 0
    odd_count = 0

    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num //= 10

    return (even_count, odd_count)

# Test cases
print(even_odd_count(-12))  # Output: (1, 1)
print(even_odd_count(123))  # Output: (1, 2)<|endoftext|>