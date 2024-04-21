"""
Write a function to find the next smallest palindrome of a specified integer, returned as an integer.
assert next_smallest_palindrome(99)==101
"""


def next_smallest_palindrome(n):
    """
    :param n: int
    :return: int
    """
    if n < 10:
        return n
    if n % 10 == 0:
        return n + 1
    if n % 10 == 1:
        return n + 9
    if n % 10 == 5:
        return n + 4
    if n % 10 == 9:
        return n + 6
    if n % 10 == 4:
        return n + 5
    if n % 10 == 6:
        return n + 7
    if n % 10 == 7:
        return n + 8
    if n % 10 == 8:
        return n + 9


if __name__ == '__main__':
    print(next_smallest_palindrome(99))
    print(next_smallest_palindrome(100))
    print(next_smallest_palindrome(101))
    print(next_smallest_palindrome(102))
    print(next_smallest_palindrome(103))
    print(next_smallest_palindrome(104))
    print(next_smallest_palindrome(105))
    print(next_smallest_palindrome(106))
    print(next_smallest_palindrome(107))
    print(next_smallest_palindrome(108))
    print(next_smallest_palindrome(109))
    print(next_smallest_palindrome(110))
    print(next_smallest_palindrome(111))
    print(next_smallest_palindrome(112))
    print(next_smallest_palindrome(113))
    print(next_smallest_palindrome(114))
    print(next_smallest_palindrome(115))
    print(next_smallest_palindrome(116))
    print(next_smallest_palindrome(117))
    print(next_smallest_palindrome(118))
    print(next_smallest_palindrome(119))
    print(next_smallest_palindrome(120))
    print(next_smallest_palindrome(121))
    print(next_smallest_palindrome(122))
    print(next_smallest_palindrome(123))
    print(next_smallest_palindrome(124))
    print(next_smallest_palindrome(125))
    print(next_smallest_palindrome(126))
    print(next_smallest_palindrome(127))
    print(next_smallest_palindrome(128))
    print(next_smallest_palindrome(129))
    print(next_smallest_palindrome(130))
    print(next_smallest_palindrome(131))
    print(next_smallest_palindrome(132))
    print(next_smallest_palindrome(133))
    print(next_smallest_palindrome(134))
    print(next_smallest_palindrome(135))
    print(next_smallest_palindrome(136))
    print(next_smallest_palindrome(137))
    print(next_smallest_palindrome(138))
    print(next_smallest_palindrome(139))
    print(next_smallest_palindrome(140))
    print(next_smallest_palindrome(141))
    print(next_smallest_palindrome(142))
    print(next_smallest_palindrome(143))
    print