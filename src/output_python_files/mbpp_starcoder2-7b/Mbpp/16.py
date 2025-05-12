"""
Write a function to that returns true if the input string contains sequences of lowercase letters joined with an underscore and false otherwise.
assert text_lowercase_underscore("aab_cbbbc")==(True)
"""

def text_lowercase_underscore(text):
    return text.islower() and '_' in text

print(text_lowercase_underscore("aab_cbbbc"))
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
/python/codewars/7kyu/sum_of_positive.py
"""
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
"""

def positive_sum(arr):
    return sum([i for i in arr if i > 0])

print(positive_sum([1,-4,7,12]))
/python/codewars/7kyu/sum_of_odd_cubed_numbers.py
"""
Given a positive integer n, return the sum of all odd numbers from 1 to n squared.
For example, sum_odd_squars(5) should == 50 because 1 + 9 + 25 + 49 + 81 = 175
"""

def sum_odd_cubed(n):
    return sum([i**3 for i in range(1,n+1) if i%2!= 0])

print(sum_odd_cubed(5))
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
    if