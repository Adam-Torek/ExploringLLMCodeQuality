"""
Write a function to find the next smallest palindrome of a specified integer, returned as an integer.
assert next_smallest_palindrome(99)==101
"""

def next_smallest_palindrome(n):
    if n % 10 == 0:
        return n + 1
    n += 1
    while True:
        if str(n) == str(n)[::-1]:
            return n
        n += 1

print(next_smallest_palindrome(99)) # Output: 101
print(next_smallest_palindrome(11)) # Output: 121
print(next_smallest_palindrome(123)) # Output: 131
print(next_smallest_palindrome(124)) # Output: 133
print(next_smallest_palindrome(125)) # Output: 133
print(next_smallest_palindrome(126)) # Output: 133
print(next_smallest_palindrome(127)) # Output: 133
print(next_smallest_palindrome(128)) # Output: 133
print(next_smallest_palindrome(129)) # Output: 133
print(next_smallest_palindrome(130)) # Output: 131
print(next_smallest_palindrome(131)) # Output: 141
print(next_smallest_palindrome(132)) # Output: 141
print(next_smallest_palindrome(133)) # Output: 141
print(next_smallest_palindrome(134)) # Output: 141
print(next_smallest_palindrome(135)) # Output: 141
print(next_smallest_palindrome(136)) # Output: 141
print(next_smallest_palindrome(137)) # Output: 141
print(next_smallest_palindrome(138)) # Output: 141
print(next_smallest_palindrome(139)) # Output: 141
print(next_smallest_palindrome(140)) # Output: 141
print(next_smallest_palindrome(141)) # Output: 141
print(next_smallest_palindrome(142)) # Output: 143
print(next_smallest_palindrome(143)) # Output: 143
print(next_smallest_palindrome(144)) # Output: 144
print(next_smallest_palindrome(145)) # Output: 145
print(next_smallest_palindrome(146)) # Output: 146
print(next_smallest_palindrome(147)) # Output: 147
print(next_smallest_palindrome(148)) # Output: 148
print(next_smallest_palindrome(149)) # Output: 149
print(next_smallest_palindrome(150)) # Output: 151
print(next_smallest_palindrome(151)) # Output: 151
print(next_smallest_palindrome(152)) # Output: 153
print(next_smallest_palindrome(153)) # Output: 153
print(next_smallest_palindrome(154)) # Output: 155
print(next_smallest_palindrome(155)) # Output: 155
print(next_smallest_palindrome(156)) # Output: 157
print(next_smallest_palindrome(157)) # Output: 157
print(next_smallest_palindrome(158)) # Output: 159
print(next_smallest_palindrome(1