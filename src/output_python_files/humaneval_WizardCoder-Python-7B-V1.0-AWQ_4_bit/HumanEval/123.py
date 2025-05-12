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
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
    odd_list = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        odd_list.append(n)
    return odd_list


# Test cases
print(get_odd_collatz(5)) # [1, 5]
print(get_odd_collatz(13)) # [1, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
print(get_odd_collatz(7)) # [1, 7]
print(get_odd_collatz(1)) # [1]
print(get_odd_collatz(2)) # []
print(get_odd_collatz(3)) # [3]
print(get_odd_collatz(10)) # [1, 10, 5, 16, 8, 4, 2, 1]
print(get_odd_collatz(17)) # [1, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
print(get_odd_collatz(25)) # [1, 25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

# Time complexity: O(log n)
# Space complexity: O(log n)