"""
Write a function to find the next smallest palindrome of a specified integer, returned as an integer.
assert next_smallest_palindrome(99)==101
"""
def next_smallest_palindrome(n):
    str_n = str(n)
    reversed_str = str_n[::-1]
    if int(reversed_str) > n:
        # if reversed string is greater than the number itself,
        # then the next smallest palindrome is the number after it
        return int(str(int(str_n)+1))
    else:
        # otherwise, we need to find the digit that is smaller in the left half
        # and larger in the right half, and swap them
        for i in range(len(str_n)//2, -1, -1):
            if int(str_n[i]) > int(str_n[len(str_n)-i-1]):
                # we found the digit, swap them and add leading zeros if needed
                left = str_n[:i]
                right = str_n[len(str_n)-i:]
                return int(left+str(int(str_n[len(str_n)-i])-1)+right)

# test cases
assert next_smallest_palindrome(99) == 101
assert next_smallest_palindrome(101) == 101
assert next_smallest_palindrome(121) == 121
assert next_smallest_palindrome(123) == 123
assert next_smallest_palindrome(120) == 119
assert next_smallest_palindrome(11) == 11
assert next_smallest_palindrome(1) == 1
assert next_smallest_palindrome(0) == 0
assert next_smallest_palindrome(-1) == -1
assert next_smallest_palindrome(-121) == -121
assert next_smallest_palindrome(-123) == -123
assert next_smallest_palindrome(-120) == -119
assert next_smallest_palindrome(-11) == -11
assert next_smallest_palindrome(-1) == -1
assert next_smallest_palindrome(-21) == -21
assert next_smallest_palindrome(-201) == -201
assert next_smallest_palindrome(-2001) == -2001
assert next_smallest_palindrome(-12345) == -12345
assert next_smallest_palindrome(-123467) == -123467
assert next_smallest_palindrome(-123456789) == -123456789
assert next_smallest_palindrome(-123456789123456789) == -123456789123456789
assert next_smallest_palindrome(-123456789123456789123456789) == -123456789123456789123456789
assert next_smallest_palindrome(-123456789123456789123456789123456789) == -123456789123456789123456789123456789
assert next_smallest_palindrome(-123456789123456789123456789123456789123456789) == -123456789123456789123456789123456789123456789
assert next_smallest_pal