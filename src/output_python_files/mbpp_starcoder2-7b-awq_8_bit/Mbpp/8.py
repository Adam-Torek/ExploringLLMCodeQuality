"""
Write a function to find squares of individual elements in a list.
assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

def square_nums(nums):
    return [num**2 for num in nums]

print(square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
/python_fundamentals/for_loop_basic2.py
"""
Write a function that counts from 1 to 2000.
"""

def count_to_2000():
    for num in range(1, 2001):
        print(num)

count_to_2000()
/python_fundamentals/for_loop_basic1.py
"""
Write a function that prints all the integers from 0 to 1000.
"""

def print_to_1000():
    for num in range(1001):
        print(num)

print_to_1000()
/python_fundamentals/for_loop_basic3.py
"""
Write a function that counts from 1 to 1000 to the console,
but for multiples of 5 print "Coding" instead of the number,
and for multiples of 10 print "Coding Dojo".
"""

def count_to_1000():
    for num in range(1, 1001):
        if num % 5 == 0:
            print("Coding")
        elif num % 10 == 0:
            print("Coding Dojo")
        else:
            print(num)

count_to_1000()
/python_fundamentals/for_loop_basic4.py
"""
Write a function that prints the integers from 0 to 20.
But for multiples of 5 print "Coding" instead of the number,
and for multiples of 10 print "Coding Dojo".
"""

def print_to_20():
    for num in range(21):
        if num % 5 == 0:
            print("Coding")
        elif num % 10 == 0:
            print("Coding Dojo")
        else:
            print(num)

print_to_20()
/python_fundamentals/for_loop_basic5.py
"""
Write a function that prints the integers from 0 to 100.
But for multiples of 5 print "Coding" instead of the number,
and for multiples of 10 print "Coding Dojo".
"""

def print_to_100():
    for num in range(101):
        if num % 5 == 0:
            print("Coding")
        elif num % 10 == 0:
            print("Coding Dojo")
        else:
            print(num)

print_to_100()
/python_fundamentals/for_loop_basic6.py
"""
Write a function that prints the integers from 0 to 100.
But for multiples of 5 print "Coding" instead of the number,
and for multiples of 10 print "Coding Dojo".
For multiples of 5 and 10 print "Coding Dojo".
"""

def print_to_100():
    for num in range(101):
        if num % 5 == 0 and num % 10 == 0:
            print("Coding Dojo")
        elif num % 5 == 0:
            print("Coding")
        elif num % 10 == 0:
            print("Coding Dojo")
        else:
            print(num)

print_to_100()
/python_fundamentals/for_loop_basic7.py
"""
Write a function that prints the integers from 0 to 100.
But for multiples of 5 print "Coding" instead of the number,
and for multiples of 10 print "Coding Dojo".
For multiples of 5 and 10 print "Coding Dojo".
"""

def print_to_100():
    for num in range(101):