"""
Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.
assert get_Char("abc") == "f"
"""

def get_Char(string):
    return chr(sum([ord(char) for char in string]) % 26 + 65)

print(get_Char("abc"))
/Python/Codewars/7kyu/Find_the_odd_int.py
"""
Given an array, find the integer that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""

def find_it(seq):
    for i in seq:
        if seq.count(i) % 2!= 0:
            return i

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
/Python/Codewars/7kyu/Find_the_divisors.py
"""
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

Example:
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
"""

def divisors(n):
    if n == 1:
        return "1 is prime"
    else:
        return [i for i in range(2, n) if n % i == 0]

print(divisors(12))
/Python/Codewars/7kyu/Find_the_next_perfect_square.py
"""
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is positive.
"""

def find_next_square(sq):
    if sq ** 0.5 % 1 == 0:
        return (sq ** 0.5 + 1) ** 2
    else:
        return -1

print(find_next_square(121))
/Python/Codewars/7kyu/Find_the_next_perfect_square.py
"""
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is positive.
"""

def find_next_square(sq):
    if sq ** 0.5 % 1 == 0:
        return (sq ** 0.5 + 1) ** 2
    else:
        return -1

print(find_next_square(121))
/Python/Codewars/7kyu/Find_the_next_perfect_square.py
"""
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is positive.
"""

def find_next_square(sq):
    if sq ** 0.5 % 1 == 0:
        return (sq ** 0.5 + 1) ** 2
    else:
        return -1

print(find_next_square(121))
/Python/Codewars/7kyu/Find_the_next_