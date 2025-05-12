"""
Write a python function to count the upper case characters in a given string.
assert upper_ctr('PYthon') == 1
"""

def upper_ctr(string):
    count = 0
    for char in string:
        if char.isupper():
            count += 1
    return count

print(upper_ctr('PYthon'))
/python/python_fundamentals/for_loop_basic1.py
"""
Basic - Print all integers from 0 to 150.
"""

for i in range(151):
    print(i)

"""
Basic - Print all the multiples of 5 from 5 to 1,000
"""

for i in range(5, 1001, 5):
    print(i)

"""
Basic - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
"""

for i in range(1, 101):
    if i % 5 == 0 and i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

"""
Basic - Print the sum of all integers from 0 to 5000.
"""

sum = 0
for i in range(5001):
    sum += i
print(sum)

"""
Basic - Print all the multiples of 6 from 6 to 60000. (inclusive).
"""

for i in range(6, 60001, 6):
    print(i)

"""
Basic - Print all the multiples of 5 from 5000 to 100. (inclusive).
"""

for i in range(5000, 101, -5):
    print(i)

"""
Basic - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
"""

for i in range(1, 101):
    if i % 5 == 0 and i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

"""
Basic - Given a list of integers, print the sum of the first and last values, and print the third value from the list.
"""

a = [1, 2, 3, 4, 5, 6]
print(a[0] + a[-1])
print(a[2])

"""
Basic - Given a list of integers, print the sum of the first and last values, and print the third value from the list.
"""

a = [1, 2, 3, 4, 5, 6]
print(a[0] + a[-1])
print(a[2])

"""
Basic - Given a list of integers, print the sum of the first and last values, and print the third value from the list.
"""

a = [1, 2, 3, 4, 5, 6]
print(a[0] + a[-1])
print(a[2])

"""
Basic - Given a list of integers, print the sum of the first and last values, and print the third value from the list.
"""

a = [1, 2, 3, 4, 5, 6]
print(a[0] + a[-1])
print(a[2])

"""
Basic - Given a list of integers, print the sum of the first and last values, and print the third value from the list.
"""

a = [1, 2, 3, 4, 5, 6]
print(a[0] + a[-1])
print(a[2])

"""
Basic - Given a list of integers, print the sum of the first and last values, and print the third value from the list.
"""

a = [1, 2, 3, 4, 5, 6]
print(a[0] + a[-1])
print(a[