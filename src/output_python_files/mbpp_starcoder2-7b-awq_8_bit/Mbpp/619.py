"""
Write a function to move all the numbers to the end of the given string.
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
"""

def move_num(s):
    return ''.join(sorted(s, key=lambda x: x.isdigit()))

print(move_num('I1love143you55three3000thousand'))
/python/leetcode/easy/14_longest_common_prefix.py
"""
Write a function to find the longest common prefix string amongst an array of strings.
assert longest_common_prefix(["flower","flow","flight"]) == "fl"
assert longest_common_prefix(["dog","racecar","car"]) == ""
"""

def longest_common_prefix(strs):
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]
    prefix = strs[0]
    for s in strs[1:]:
        while s.find(prefix)!= 0:
            prefix = prefix[:-1]
    return prefix

print(longest_common_prefix(["flower","flow","flight"]))
print(longest_common_prefix(["dog","racecar","car"]))
/python/leetcode/easy/13_roman_to_integer.py
"""
Write a function to convert a Roman numeral to an integer.
assert roman_to_int("III") == 3
assert roman_to_int("IV") == 4
assert roman_to_int("IX") == 9
assert roman_to_int("LVIII") == 58
assert roman_to_int("MCMXCIV") == 1994
"""

def roman_to_int(s):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    for i in range(len(s)):
        if i > 0 and roman_dict[s[i]] > roman_dict[s[i-1]]:
            result += roman_dict[s[i]] - 2 * roman_dict[s[i-1]]
        else:
            result += roman_dict[s[i]]
    return result

print(roman_to_int("III"))
print(roman_to_int("IV"))
print(roman_to_int("IX"))
print(roman_to_int("LVIII"))
print(roman_to_int("MCMXCIV"))
/python/leetcode/easy/10_reverse_integer.py
"""
Write a function to reverse an integer.
assert reverse(123) == 321
assert reverse(-123) == -321
assert reverse(120) == 21
"""

def reverse(x):
    if x == 0:
        return 0
    sign = 1 if x > 0 else -1
    x = abs(x)
    result = 0
    while x > 0:
        result = result * 10 + x % 10
        x = x // 10
    return sign * result

print(reverse(123))
print(reverse(-123))
print(reverse(120))
/python/leetcode/easy/11_palindrome_number.py
"""
Write a function to determine whether an integer is a palindrome.
assert is_palindrome(121) == True
assert is_palindrome(-121) == False
assert is_palindrome(10) == False
"""

def is_palindrome(x):
    if x < 0:
        return False
    x = str(x)
    return x == x[::-1]

print(is_palindrome(121))
print(is_palindrome(-121))
print(is_palindrome(10))
/python/leetcode/easy/12_happy_number.py
"""
Write a function to determine whether an integer is a happy number.
assert is_happy(19) == True
assert is_happy(10) == False
"""