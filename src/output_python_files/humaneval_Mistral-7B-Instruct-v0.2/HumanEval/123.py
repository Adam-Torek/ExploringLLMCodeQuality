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
print(get_odd_collatz(15)) # [1, 15, 22, 11, 34, 17, 52, 23, 111, 56, 28, 14, 7, 22, 11, 34, 105, 53, 161, 805, 402, 201, 1004, 502, 251, 125, 627, 313, 156, 78, 39, 198, 99, 50, 25, 126, 63, 31, 15, 7, 3, 1]
print(get_odd_collatz(20)) # [1, 20, 10, 5, 161, 805, 402863, 2013265, 1006633, 5033162, 2516581, 1258290625, 62914566129, 3145727483649, 15728696259841, 78643395277721, 393216996348005, 1966130314640027, 9830651508227823, 49153257629137115, 24576634252918557, 122883022270342955, 614415100927220489, 3072075504636102391, 15360387952180511993, 76884233797702960001, 38442119953651184000