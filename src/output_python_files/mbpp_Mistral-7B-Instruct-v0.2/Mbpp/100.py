"""
Write a function to find the next smallest palindrome of a specified integer, returned as an integer.
assert next_smallest_palindrome(99)==101
"""
def next_smallest_palindrome(n):
    str_n = str(n)
    if int(str_n[::-1]) > n:
        return int(str(int(str_n[::-1]) + 1))
    else:
        for i in range(len(str_n)-1, -1, -1):
            if str_n[i] > str_n[i+1]:
                j = len(str_n) - i - 1
                str_n = str_n[:i] + str_n[j] + str_n[i+1:j] + str_n[i+1:]
                break
        return int(str_n)

assert next_smallest_palindrome(99) == 101
assert next_smallest_palindrome(100) == 101
assert next_smallest_palindrome(123) == 121
assert next_smallest_palindrome(120) == 119
assert next_smallest_palindrome(111) == 111
assert next_smallest_palindrome(110) == 101
assert next_smallest_palindrome(101) == 101
assert next_smallest_palindrome(1) == 1
assert next_smallest_palindrome(0) == 0
assert next_smallest_palindrome(-1) == -1
assert next_smallest_palindrome(-10) == -11
assert next_smallest_palindrome(-121) == -120
assert next_smallest_palindrome(-123) == -121
assert next_smallest_palindrome(-120) == -119
assert next_smallest_palindrome(-111) == -111
assert next_smallest_palindrome(-110) == -101
assert next_smallest_palindrome(-101) == -101
assert next_smallest_palindrome(-1) == -1
assert next_smallest_palindrome(-21) == -20
assert next_smallest_palindrome(-20) == -19
assert next_smallest_palindrome(-2) == -2
assert next_smallest_palindrome(-1223) == -1221
assert next_smallest_palindrome(-1221) == -1221
assert next_smallest_palindrome(-1220) == -1211
assert next_smallest_palindrome(-1211) == -1211
assert next_smallest_palindrome(-1210) == -1201
assert next_smallest_palindrome(-1201) == -1201
assert next_smallest_palindrome(-120) == -119
assert next_smallest_palindrome(-119) == -119
assert next_smallest_palindrome(-118) == -117
assert next_smallest_palindrome(-117) == -117
assert next_smallest_palindrome(-116) == -115
assert next_smallest_palindrome(-115) == -115
assert next_smallest_palindrome(-114) == -113
assert next_smallest_palindrome(-113) == -113
assert next_smallest_palindrome(-112) == -111
assert next_smallest_palindrome(-111) == -111
assert next_smallest_palindrome(-110) == -101
assert next_smallest_palindrome(-101) == -101
assert next_smallest_palindrome(-100) == -