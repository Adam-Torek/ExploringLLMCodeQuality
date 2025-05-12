"""
Write a function to merge three lists into a single sorted list.
assert merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])==[4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]
"""

def merge_sorted_list(list1, list2, list3):
    list1.extend(list2)
    list1.extend(list3)
    list1.sort()
    return list1

print(merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48]))
/python/python_fundamentals/for_loop_basic2.py
"""
Basic -1

Multiples of 3 and 5

Print all the integers from 1 to 1000.

For multiples of 3 print "Fizz" instead of the number.

For multiples of 5 print "Buzz" instead of the number.

For numbers which are multiples of both 3 and 5 print "FizzBuzz" instead of the number.
"""

for i in range(1, 1001):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
/python/python_fundamentals/for_loop_basic1.py
"""
Basic -1

Print all integers from 0 to 150.

Have the program count by 5's in increments of 1.

Start at zero.
"""

for i in range(0, 151, 5):
    print(i)
/python/python_fundamentals/for_loop_basic3.py
"""
Basic -2

Countdown by Fours

Print positive numbers starting at 2018, counting down by fours.

Exclude 0.
"""

for i in range(2018, 0, -4):
    print(i)
/python/python_fundamentals/for_loop_basic4.py
"""
Basic -3

Flexible Counter

Set three variables: lowNum, highNum, mult.

Have the program count from lowNum to highNum, by multiples of mult.

For example, if lowNum=2, highNum=9, mult=3,

the loop should print out: 2 5 8 (on successive lines)
"""

lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum + 1, mult):
    print(i)
/python/python_fundamentals/for_loop_basic5.py
"""
Basic -4

Print and Count

Print the integers from 0 to 100.

But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".

For numbers which are multiples of both three and five print "FizzBuzz".
"""

for i in range(0, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
/python/python_fundamentals/for_loop_basic6.py
"""
Basic -5

Multiples of 10

Print the multiples of 5 from 5 to 1