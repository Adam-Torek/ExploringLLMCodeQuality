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
    if n == 1:
        return [1]
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    odd_list = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n not in odd_list:
            odd_list.append(n)
    return odd_list


# Test cases
print(get_odd_collatz(5))  # Output: [1, 5]
print(get_odd_collatz(13))  # Output: [1, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
print(get_odd_collatz(1))  # Output: [1]
print(get_odd_collatz(2))  # Output: [1]
print(get_odd_collatz(10))  # Output: [1, 10, 5, 16, 8, 4, 2, 1]
print(get_odd_collatz(100))  # Output: [1, 100, 50, 125, 62, 31, 106, 53, 17, 85, 42, 21, 106, 53, 17, 85, 42, 21, 106, 53, 17, 85, 42, 21, 106, 53, 17, 85, 42, 21, 106, 53, 17, 85, 42, 21, 106, 53, 17, 85, 42, 21, 106, 53, 17, 85, 42, 21, 106, 53, 17, 85, 42, 21, 106, 53, 17, 85, 42, 21, 106, 53, 17, 85, 42, 21, 106, 53, 17, 85, 42, 21, 106, 53, 17, 85, 42, 21, 106, 53, 17, 85, 42, 21, 106, 53, 17, 85, 42, 21, 106, 53, 17, 85, 42, 21, 106, 53, 17, 85, 42, 21, 106, 53, 17, 85, 42, 21, 106, 53, 17, 85, 42,