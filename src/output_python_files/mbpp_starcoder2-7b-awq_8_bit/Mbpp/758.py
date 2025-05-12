"""
Write a function to count lists within a list. The function should return a dictionary where every list is converted to a tuple and the value of such tuple is the number of its occurencies in the original list.
assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] )=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
"""

def unique_sublists(lst):
    d = {}
    for i in lst:
        d[tuple(i)] = lst.count(i)
    return d

print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))
/python/python_fundamentals/for_loop_basic2.py
"""
Basic - 1

Multiples of 3 and 5

Print all the integers from 1 to 1000. For multiples of 3 print "Fizz" instead of the number and for multiples of 5 print "Buzz". For numbers which are multiples of both 3 and 5 print "FizzBuzz".
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
Basic - 1

Print all integers from 0 to 150.
"""

for i in range(151):
    print(i)
/python/python_fundamentals/for_loop_basic3.py
"""
Basic - 3

Multiples of 3 and 5

Print the sum of all multiples of 3 and 5 between 1 and 1000.
"""

sum = 0
for i in range(1, 1001):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(sum)
/python/python_fundamentals/for_loop_basic4.py
"""
Basic - 4

Countdown by Fours

Print positive numbers starting at 2018, counting down by fours (exclude 0).
"""

for i in range(2018, 0, -4):
    print(i)
/python/python_fundamentals/for_loop_basic5.py
"""
Basic - 5

Flexible Counter

Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
"""

lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)
/python/python_fundamentals/for_loop_basic6.py
"""
Basic - 6

Print and Count

Print all integers from 0 to 1000. But for multiples of 5 print "Coding" instead of the number and for multiples of 10 print "Coding Dojo". For example, if we count to 20, we should see the following:

You should see the following:
1
2
Coding
4
Coding
Coding Dojo
7
8
Coding
Coding Dojo
11
Coding
13
14
Coding Dojo
16
17
Coding
Coding Dojo
19
Coding Dojo
"""

for i in range(1, 1001):
    if i % 5 == 0 and i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")