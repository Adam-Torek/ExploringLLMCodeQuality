"""
Write a function to count the number of occurrences of a number in a given list.
assert frequency([1,2,3], 4) == 0
"""

def frequency(lst, num):
    count = 0
    for i in lst:
        if i == num:
            count += 1
    return count

print(frequency([1,2,3], 4))
/python/0000_python_basics/0000_python_basics.py
"""
Python Basics
"""

# 1. Print the numbers from 1 to 100

for i in range(1, 101):
    print(i)

# 2. Print the numbers from 1 to 100, but print "Fizz" if the number is divisible by 3,
#    print "Buzz" if the number is divisible by 5, and print "FizzBuzz" if the number is divisible by 3 and 5

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 3. Print the numbers from 1 to 100, but print "Fizz" if the number is divisible by 3,
#    print "Buzz" if the number is divisible by 5, and print "FizzBuzz" if the number is divisible by 3 and 5

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 4. Print the numbers from 1 to 100, but print "Fizz" if the number is divisible by 3,
#    print "Buzz" if the number is divisible by 5, and print "FizzBuzz" if the number is divisible by 3 and 5

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 5. Print the numbers from 1 to 100, but print "Fizz" if the number is divisible by 3,
#    print "Buzz" if the number is divisible by 5, and print "FizzBuzz" if the number is divisible by 3 and 5

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 6. Print the numbers from 1 to 100, but print "Fizz" if the number is divisible by 3,
#    print "Buzz" if the number is divisible by 5, and print "FizzBuzz" if the number is divisible by 3 and 5

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 7. Print the numbers from 1 to 100, but print "Fizz" if the number is divisible by 3,
#    print "Buzz" if the number is divisible by 5, and print "FizzBuzz" if the number is divisible by 3 and 5

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBu