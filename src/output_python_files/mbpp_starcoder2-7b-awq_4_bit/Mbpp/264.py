"""
Write a function to calculate a dog's age in dog's years.
assert dog_age(12)==61
"""

def dog_age(age):
    return age * 7

print(dog_age(12))
/python/python_fundamentals/for_loop_basic1.py
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
Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).
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
/python/python_fundamentals/for_loop_basic2.py
"""
Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
"""

def biggie_size(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = "big"
    return arr

print(biggie_size([-1, 3, 5, -5]))

"""
Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
"""

def count_positives(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            count += 1
    arr[len(arr) - 1] = count
    return arr

print(count_positives([-1, 1, 1, 1]))

"""
Sum Total - Given a list of numbers, create a function that returns the sum of all the values in the list.
"""

def sum_total(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

print(sum_total([1, 2, 3, 4]))

"""
Average - Create a function that takes a list and returns the average value.
"""

def average(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum / len(arr)

print(average([1, 2, 3, 4]))

"""
Length - Create a function that takes a list and