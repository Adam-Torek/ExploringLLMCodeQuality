"""
Write a function to round every number of a given list of numbers and print the total sum multiplied by the length of the list.
assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243
"""

def round_and_sum(numbers):
    total = 0
    for number in numbers:
        total += round(number)
    return total * len(numbers)

print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]))
/python/python_fundamentals/for_loop_basic1.py
"""
Basic -1: Print integers from 0 to 1000.
"""

for i in range(0, 1001):
    print(i)
/python/python_fundamentals/for_loop_basic2.py
"""
Basic 2: Multiples of Five
Print multiples of 5 from 5 to 1,000,000.
"""

for i in range(5, 1000001, 5):
    print(i)
/python/python_fundamentals/for_loop_basic3.py
"""
Basic 3: Countdown by Fours
Print positive numbers starting at 2018, counting down by fours (exclude 0).
"""

for i in range(2018, 0, -4):
    print(i)
/python/python_fundamentals/for_loop_basic4.py
"""
Basic 4: Flexible Counter
Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult.
For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
"""

lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)
/python/python_fundamentals/for_loop_basic5.py
"""
Basic 5: Multiples of Six
Print multiples of 6 up to 60,000,000.
"""

for i in range(6, 60000001, 6):
    print(i)
/python/python_fundamentals/for_loop_basic6.py
"""
Basic 6: Print the Sum
Print the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

a = [1, 2, 5, 10, 255, 3]

sum = 0
for i in a:
    sum += i

print(sum)
/python/python_fundamentals/for_loop_basic7.py
"""
Basic 7: Print Average
Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

a = [1, 2, 5, 10, 255, 3]

sum = 0
for i in a:
    sum += i

print(sum / len(a))
/python/python_fundamentals/for_loop_basic8.py
"""
Basic 8: Countdown from the Center
Create a program that prints all the numbers from 100 to 1,000,000.
"""

for i in range(100, 1000001):
    print(i)
/python/python_fundamentals/for_loop_basic9.py
"""
Basic 9: Multiples of Three
Print multiples of 3 from 0 to 1000.
"""

for i in range(0, 1001