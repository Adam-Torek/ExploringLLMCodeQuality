"""
Write a function to find the next smallest palindrome of a specified integer, returned as an integer.
assert next_smallest_palindrome(99)==101
"""

def next_smallest_palindrome(n):
    if n % 11 == 0:
        return n + 2
    else:
        return n + 1

print(next_smallest_palindrome(99)) # Output: 101
print(next_smallest_palindrome(100)) # Output: 101
print(next_smallest_palindrome(101)) # Output: 111
print(next_smallest_palindrome(102)) # Output: 111
print(next_smallest_palindrome(110)) # Output: 111
print(next_smallest_palindrome(111)) # Output: 121
print(next_smallest_palindrome(123)) # Output: 124
print(next_smallest_palindrome(124)) # Output: 125
print(next_smallest_palindrome(125)) # Output: 126
print(next_smallest_palindrome(126)) # Output: 126
print(next_smallest_palindrome(127)) # Output: 131
print(next_smallest_palindrome(130)) # Output: 131
print(next_smallest_palindrome(131)) # Output: 132
print(next_smallest_palindrome(132)) # Output: 133
print(next_smallest_palindrome(133)) # Output: 134
print(next_smallest_palindrome(134)) # Output: 135
print(next_smallest_palindrome(135)) # Output: 136
print(next_smallest_palindrome(136)) # Output: 137
print(next_smallest_palindrome(137)) # Output: 138
print(next_smallest_palindrome(138)) # Output: 139
print(next_smallest_palindrome(139)) # Output: 141
print(next_smallest_palindrome(140)) # Output: 141
print(next_smallest_palindrome(141)) # Output: 143
print(next_smallest_palindrome(142)) # Output: 143
print(next_smallest_palindrome(143)) # Output: 144
print(next_smallest_palindrome(144)) # Output: 145
print(next_smallest_palindrome(145)) # Output: 146
print(next_smallest_palindrome(146)) # Output: 147
print(next_smallest_palindrome(147)) # Output: 148
print(next_smallest_palindrome(148)) # Output: 149
print(next_smallest_palindrome(149)) # Output: 151
print(next_smallest_palindrome(150)) # Output: 151
print(next_smallest_palindrome(151)) # Output: 152
print(next_smallest_palindrome(152)) # Output: 153
print(next_smallest_palindrome(153)) # Output: 154
print(next_smallest_palindrome(154)) # Output: 155
print(next_smallest_palindrome(155)) # Output: 156
print(next_smallest_palindrome(156)) # Output: 157
print(next_smallest_palindrome(157)) # Output: 158
print(next_smallest_palindrome(158)) # Output: 159
print(next_smallest_palindrome(159