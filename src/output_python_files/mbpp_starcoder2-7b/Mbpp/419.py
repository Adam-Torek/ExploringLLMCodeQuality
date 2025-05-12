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
/python/python_fundamentals/for_loop_basic_1.py
"""
Basic - Print all integers from 0 to 150.
"""

for i in range(0, 151):
    print(i)

"""
Multiples of Five - Print all the multiples of 5 from 5 to 1,000
"""

for i in range(5, 1001, 5):
    print(i)

"""
Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
"""

for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

"""
Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
"""

sum = 0
for i in range(0, 500001, 2):
    sum += i
print(sum)

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
/python/python_fundamentals/functions_intermediate_1.py
"""
Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
assert countdown(5) == [5,4,3,2,1,0]
"""

def countdown(number):
    new_list = []
    for i in range(number, -1, -1):
        new_list.append(i)
    return new_list

print(countdown(5))

"""
Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
assert print_and_return([1,2]) == 2
"""

def print_and_return(numbers):
    print(numbers[0])
    return numbers[1]

print(print_and_return([1,2]))

"""
First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
assert first_plus_length([1,2,3,4,5]) == 6
"""

def first_plus_length(numbers):
    return numbers[0] + len(numbers)

print(first_plus_length([1,2,3,4,5]))

"""
Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than