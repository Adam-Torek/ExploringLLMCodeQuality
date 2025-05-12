"""
Write a function to find squares of individual elements in a list.
assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

def square_nums(nums):
    return [num**2 for num in nums]

print(square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
/python/python_fundamentals/for_loop_basic_1.py
"""
Basic - Print all integers from 0 to 150.
"""

for i in range(0, 151):
    print(i)

"""
Basic II - Print all the multiples of 5 from 5 to 1,000
"""

for i in range(5, 1001, 5):
    print(i)

"""
Basic III - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
"""

for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

"""
Basic IV - Add odd integers from 0 to 500,000, and print the final sum.
"""

sum = 0
for i in range(0, 500001, 2):
    sum += i
print(sum)

"""
Basic V - Print positive numbers starting at 2018, counting down by fours.
"""

for i in range(2018, 0, -4):
    print(i)

"""
FizzBuzz - Print integers 1 to 100. If divisible by 5, print "Fizz", if divisible by 3, print "Buzz", if divisible by both, print "FizzBuzz".
"""

for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

"""
Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
"""

for i in range(2018, 0, -4):
    print(i)

"""
Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
"""

lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)
/python/python_fundamentals/for_loop_basic_2.py
"""
Basic - Print values of the list [7,22,43,21,67,453,4,32,56,68,55,17,33].
"""

list = [7, 22, 43, 21, 67, 453, 4, 32, 56, 68, 55, 17, 33]
for i in list:
    print(i)

"""
Basic II - Print the sum of all the values in the list.
"""

list = [7, 22, 43, 21, 67, 453, 4, 32, 56, 68, 55, 17, 33]
sum = 0
for i in list:
    sum += i
print(sum)

"""
Basic III - Create a function that