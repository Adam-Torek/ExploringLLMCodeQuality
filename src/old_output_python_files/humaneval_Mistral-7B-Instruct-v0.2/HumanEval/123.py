def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """
    odd_numbers = []
    sequence = [n]
    while sequence[-1] != 1:
        if sequence[-1] % 2 == 0:
            sequence.append(sequence[-1] // 2)
        else:
            sequence.append(3 * sequence[-1] + 1)
        if sequence[-1] % 2 == 1:
            odd_numbers.append(sequence[-1])
    odd_numbers.append(1)
    return odd_numbers

# Test cases
print(get_odd_collatz(1)) # [1]
print(get_odd_collatz(3)) # [1, 3]
print(get_odd_collatz(5)) # [1, 5]
print(get_odd_collatz(10)) # [1, 5, 13, 20, 10]
print(get_odd_collatz(15)) # [1, 15, 22, 11, 34, 17, 52, 23, 111, 56, 28, 14, 7, 22, 11]
print(get_odd_collatz(20)) # [1, 20, 10, 5, 16, 8, 4, 2, 1]
print(get_odd_collatz(21)) # [1, 21, 34, 17, 52, 23, 11, 34, 17, 52, 23, 11, 34, 17, 52, 23, 11]
print(get_odd_collatz(22)) # [1, 22, 11, 34, 17, 52, 23, 11, 34, 17, 52, 23, 11, 34, 17, 52, 23, 11]
print(get_odd_collatz(23)) # [1, 23]
print(get_odd_collatz(24)) # [1, 24, 12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
print(get_odd_collatz(25)) # [1, 25, 126, 63, 34, 17, 52, 23, 11, 34, 17, 52, 23, 11, 34, 17, 52, 23, 11]
print(get_odd_collatz(26)) # [1, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
print(get_odd_collatz(27)) # [1, 27, 145, 72, 36, 18, 9, 28, 14, 7, 22, 11,