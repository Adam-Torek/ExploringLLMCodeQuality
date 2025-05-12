"""
Write a function to extract specified size of strings from a given list of string values.
assert extract_string(['Python', 'list', 'exercises', 'practice','solution'],8)==['practice','solution']
"""
def extract_string(lst,size):
    return lst[-size:]

print(extract_string(['Python', 'list', 'exercises', 'practice','solution'],8))
/python_basics/python_basics_1.py
"""
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""
import datetime
print(datetime.datetime.now())
/python_basics/python_basics_10.py
"""
Write a Python program to get the volume of a sphere with radius 6.
"""
import math
def volume(r):
    return 4/3*math.pi*r**3
print(volume(6))
/python_basics/python_basics_12.py
"""
Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
"""
def sum_three(a,b,c):
    if a==b==c:
        return 3*(a+b+c)
    else:
        return a+b+c
print(sum_three(1,2,3))
print(sum_three(1,1,1))
/python_basics/python_basics_11.py
"""
Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""
def test(n):
    return (abs(1000-n)<=100) or (abs(2000-n)<=100)
print(test(1000))
print(test(1001))
print(test(1999))
print(test(2000))
print(test(2001))
/python_basics/python_basics_13.py
"""
Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
"""
def sum_two(a,b):
    if 15<=a+b<=20:
        return 20
    else:
        return a+b
print(sum_two(10,10))
print(sum_two(15,15))
print(sum_two(15,16))
print(sum_two(15,17))
print(sum_two(15,18))
print(sum_two(15,19))
print(sum_two(15,20))
print(sum_two(15,21))
/python_basics/python_basics_14.py
"""
Write a Python program to sum of three given integers. However, if two of the values are equal then return three times of their sum.
"""
def sum_three(a,b,c):
    if a==b==c:
        return 3*(a+b+c)
    else:
        return a+b+c
print(sum_three(1,2,3))
print(sum_three(1,1,1))
print(sum_three(1,2,1))
/python_basics/python_basics_15.py
"""
Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
"""
def sum_two(a,b):
    if 15<=a+b<=20:
        return 20
    else:
        return a+b
print(sum_two(10,10))
print(sum_two(15,15))
print(sum_two(15,16))
print(sum_two(15,17))
print(sum_two(15,18))
print(sum_two(15,19))
print(sum_two(15,20))
print(sum_two(15,21))
/python_basics/python_basics_16.py
"""
Write a Python program to sum of three given integers. However, if