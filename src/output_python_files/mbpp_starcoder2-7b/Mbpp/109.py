"""
Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.
assert odd_Equivalent("011001",6) == 3
"""

def odd_Equivalent(s,n):
    return sum(int(s[i])!= int(s[i-n]) for i in range(n,len(s)))

print(odd_Equivalent("011001",6))<file_sep>/Python/CodeWars/7kyu/Find_the_odd_int.py
"""
Given an array, find the int that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
"""

def find_it(seq):
    for i in seq:
        if seq.count(i) % 2!= 0:
            return i

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))<file_sep>/Python/CodeWars/7kyu/Find_the_divisors.py
"""
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
"""

def divisors(integer):
    return [i for i in range(2,integer) if integer % i == 0] or "{} is prime".format(integer)

print(divisors(12))<file_sep>/Python/CodeWars/7kyu/Find_the_divisors.py
"""
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
"""

def divisors(integer):
    return [i for i in range(2,integer) if integer % i == 0] or "{} is prime".format(integer)

print(divisors(12))<file_sep>/Python/CodeWars/7kyu/Find_the_divisors.py
"""
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
"""

def divisors(integer):
    return [i for i in range(2,integer) if integer % i == 0] or "{} is prime".format(integer)

print(divisors(12))<file_sep>/Python/CodeWars/7kyu/Find_the_divisors.py
"""
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
"""

def divisors(integer):
    return [i for i in range(2,integer) if integer % i == 0] or "{} is prime".format(integer)

print(divisors(12))<file_sep>/Python/CodeWars/7kyu/Find_the_divisors.py
"""
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
"""

def divisors(integer):
    return [i for