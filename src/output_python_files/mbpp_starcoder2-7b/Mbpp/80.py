"""
Write a function to find the nth tetrahedral number.
assert tetrahedral_number(5) == 35
"""

def tetrahedral_number(n):
    return n * (n + 1) * (n + 2) * (n + 3) / 24

print tetrahedral_number(5)
/python/0001-1000/0031-0100/0077-0080/0078-0080/0079-0080/0079.py
"""
https://projecteuler.net/problem=79

A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""

from collections import defaultdict

def solve():
    with open('0079.txt') as f:
        data = f.read().splitlines()

    # build graph
    graph = defaultdict(list)
    for line in data:
        for i in range(len(line) - 1):
            graph[line[i]].append(line[i + 1])

    # topological sort
    result = []
    while graph:
        for node in graph:
            if not graph[node]:
                result.append(node)
                del graph[node]
                break
        else:
            return 'No solution'

    return ''.join(result)

print solve()
/python/0001-1000/0001-0100/0001-0010/0008-0010/0009.py
"""
https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def solve():
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c

print solve()
/python/0001-1000/0001-0100/0001-0010/0001-0010/0001.py
"""
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def solve():
    return sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)

print solve()
/python/0001-1000/0001-0100/0001-0010/0003-0010/0004.py
"""
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_pal