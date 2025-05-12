"""
Write a python function to reverse only the vowels of a given string (where y is not a vowel).
assert reverse_vowels("Python") == "Python"
"""

def reverse_vowels(string):
    vowels = "aeiou"
    vowels_list = []
    for char in string:
        if char in vowels:
            vowels_list.append(char)
    vowels_list.reverse()
    new_string = ""
    for char in string:
        if char in vowels:
            new_string += vowels_list.pop()
        else:
            new_string += char
    return new_string

print(reverse_vowels("Python"))
/python/codewars/7kyu/sum_of_digits_digital_root.py
"""
In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

Here's how it works (Ruby example given):

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15...
=> 1 + 5
=> 6

digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24...
=> 2 + 4
=> 6

digital_root(493193)
=> 4 + 9 + 3 + 1 + 9 + 3
=> 29...
=> 2 + 9
=> 11...
=> 1 + 1
=> 2
"""

def digital_root(n):
    if n < 10:
        return n
    else:
        return digital_root(sum([int(i) for i in str(n)]))

print(digital_root(132189))
/python/codewars/7kyu/sum_of_odd_cubed_numbers.py
"""
Given a positive integer n, return the sum of all odd numbers from 1 to n squared.

For example, sum_odd_squars(5) should return 50, because 1 + 9 + 25 = 35.
"""

def sum_odd_cubed(n):
    return sum([i**3 for i in range(1, n+1) if i % 2!= 0])

print(sum_odd_cubed(5))
/python/codewars/7kyu/sum_of_odd_numbers.py
"""
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8
"""

def row_sum_odd_numbers(n):
    return sum([i for i in range(1, n*2, 2)])

print(row_sum_odd_numbers(1))
/python/codewars/7kyu/sum_of_digits_digital_root.py
"""
In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

Here's how it works (Ruby example given):

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15...
=> 1 +