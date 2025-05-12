"""
Write a python function to find smallest number in a list.
assert smallest_num([10, 20, 1, 45, 99]) == 1
"""

def smallest_num(list):
    smallest = list[0]
    for i in list:
        if i < smallest:
            smallest = i
    return smallest

print(smallest_num([10, 20, 1, 45, 99]))
/python/python_fundamentals/for_loop_basic2.py
"""
Write a python program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

a = [1, 2, 5, 10, 255, 3]

sum = 0
for i in a:
    sum += i

print(sum)
/python/python_fundamentals/for_loop_basic1.py
"""
Write a python program that prints all the integers from 0 to 1000.
"""

for i in range(0, 1001):
    print(i)
/python/python_fundamentals/for_loop_basic3.py
"""
Write a python program that multiplies all the numbers in the list by 5.
a = [1, 2, 5, 10, 255, 3]
"""

a = [1, 2, 5, 10, 255, 3]

for i in range(len(a)):
    a[i] *= 5

print(a)
/python/python_fundamentals/for_loop_basic4.py
"""
Write a python program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

a = [1, 2, 5, 10, 255, 3]

sum = 0
for i in a:
    sum += i

print(sum)

# or

print(sum(a))
/python/python_fundamentals/for_loop_basic5.py
"""
Write a python program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

a = [1, 2, 5, 10, 255, 3]

sum = 0
for i in a:
    sum += i

print(sum / len(a))
/python/python_fundamentals/for_loop_basic6.py
"""
Write a python program that prints the maximum value in the list: a = [1, 2, 5, 10, 255, 3]
"""

a = [1, 2, 5, 10, 255, 3]

max = a[0]
for i in a:
    if i > max:
        max = i

print(max)
/python/python_fundamentals/for_loop_basic7.py
"""
Write a python program that prints the minimum value in the list: a = [1, 2, 5, 10, 255, 3]
"""

a = [1, 2, 5, 10, 255, 3]

min = a[0]
for i in a:
    if i < min:
        min = i

print(min)
/python/python_fundamentals/for_loop_basic8.py
"""
Write a python program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

a = [1, 2, 5, 10, 255, 3]

sum = 0
for i in a:
    sum += i

print(sum / len(a))
/python/python_fundamentals/for_loop