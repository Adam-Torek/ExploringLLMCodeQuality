"""
Write a python function to return the negative numbers in a list.
assert neg_nos([-1,4,5,-6]) == [-1,-6]
"""

def neg_nos(nums):
    return [num for num in nums if num < 0]

print(neg_nos([-1,4,5,-6]))
/python/001_python_basics/001_python_basics.py
"""
Python Basics
"""

# 1. Print the numbers from 1 to 100

for i in range(1, 101):
    print(i)

# 2. Print the numbers from 1 to 100, but if the number is divisible by 3, print "Fizz" instead of the number

for i in range(1, 101):
    if i % 3 == 0:
        print("Fizz")
    else:
        print(i)

# 3. Print the numbers from 1 to 100, but if the number is divisible by 3, print "Fizz" instead of the number, and if the number is divisible by 5, print "Buzz" instead of the number

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 4. Print the numbers from 1 to 100, but if the number is divisible by 3, print "Fizz" instead of the number, if the number is divisible by 5, print "Buzz" instead of the number, and if the number is divisible by 3 and 5, print "FizzBuzz" instead of the number

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 5. Print the numbers from 1 to 100, but if the number is divisible by 3, print "Fizz" instead of the number, if the number is divisible by 5, print "Buzz" instead of the number, and if the number is divisible by 3 and 5, print "FizzBuzz" instead of the number, but if the number is divisible by 7, print "Bang" instead of the number

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
        print("FizzBuzzBang")
    elif i % 3 == 0 and i % 7 == 0:
        print("FizzBang")
    elif i % 5 == 0 and i % 7 == 0:
        print("BuzzBang")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 7 == 0:
        print("Bang")
    else:
        print(i)

# 6. Print the numbers from 1 to 100, but if the number is divisible by 3, print "Fizz" instead of the number, if the number is divisible by 5, print "Buzz" instead of the number, and if the number is divisible by 3 and 5, print "FizzBuzz" instead of the number, but if the number is divisible by 7, print "Bang" instead of the number, and if the number is divisible by 3 and 7, print "FizzBang" instead of the number, and if the number is divisible by 5 and 7, print "BuzzBang" instead of the number, and if the number is divisible by 3, 5, and 7, print "FizzBuzzBang" instead of the number

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0 and i %