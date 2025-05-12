"""
Write a function to return the sum of all divisors of a number.
assert sum_div(8)==7
"""
def sum_div(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum += i
    return sum

print(sum_div(8))
/python/python_fundamentals/for_loop_basic2.py
"""
Write a function that counts from 1 to 2000.
"""
def count_to_2000():
    for i in range(1,2001):
        print(i)

count_to_2000()
/python/python_fundamentals/for_loop_basic1.py
"""
Write a function that prints all the integers from 0 to 150.
"""
def count_to_150():
    for i in range(0,151):
        print(i)

count_to_150()
/python/python_fundamentals/for_loop_basic3.py
"""
Write a function that prints all the multiples of 5 from 5 to 1,000,000.
"""
def count_to_1000000():
    for i in range(5,1000001,5):
        print(i)

count_to_1000000()
/python/python_fundamentals/for_loop_basic4.py
"""
Write a function that prints the odd numbers from 1 to 1000.
"""
def count_to_1000():
    for i in range(1,1001):
        if i%2!= 0:
            print(i)

count_to_1000()
/python/python_fundamentals/for_loop_basic5.py
"""
Write a function that prints and returns the sum of all the values from 1 to 5000000.
"""
def count_to_5000000():
    sum = 0
    for i in range(1,5000001):
        sum += i
    print(sum)
    return sum

count_to_5000000()
/python/python_fundamentals/for_loop_basic6.py
"""
Write a function that prints the odd numbers from 1 to 1000.
"""
def count_to_1000():
    for i in range(1,1001):
        if i%2!= 0:
            print(i)

count_to_1000()

"""
Write a function that prints and returns the sum of all the values from 1 to 5000000.
"""
def count_to_5000000():
    sum = 0
    for i in range(1,5000001):
        sum += i
    print(sum)
    return sum

count_to_5000000()

"""
Write a function that accepts a number as a parameter and counts, prints, and returns the sum of all the values from 1 to that number.
"""
def count_to_n(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    print(sum)
    return sum

count_to_n(100)
/python/python_fundamentals/for_loop_basic7.py
"""
Write a function that accepts start and end numbers, and prints and returns the sum of all the even values from start to end.
"""
def count_to_n(start,end):
    sum = 0
    for i in range(start,end+1):
        if i%2 == 0:
            sum += i
    print(sum)
    return sum

count_to_n(1,100)
/python/python_fundamentals/for_loop_basic8.py
"""
Write a function that accepts start and end numbers, and prints and returns the sum of all the values from start to end,
"""
def count_to_n(start,end):
    sum = 0
    for i in range(start,end+1):
        sum += i
    print(sum)
    return sum

count_to_n(1,100)

"""