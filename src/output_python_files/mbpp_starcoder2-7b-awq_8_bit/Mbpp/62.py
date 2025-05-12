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

for i in range(1001):
    print(i)
/python/python_fundamentals/for_loop_basic3.py
"""
Write a python program that multiplies all the numbers in the list a = [1, 2, 5, 10, 255, 3] by 5 and prints the new list.
"""

a = [1, 2, 5, 10, 255, 3]
new_list = []
for i in a:
    new_list.append(i * 5)
print(new_list)
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

a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in range(len(a)):
    sum += a[i]
print(sum)
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
Write a python program that prints all the numbers from 0 to 100 that are divisible by 5 and 3.
"""

for i in range(101):
    if i % 5 == 0 and i % 3 == 0:
        print(i)
/python/python_fundamentals/for_loop_basic7.py
"""
Write a python program that prints all the multiples of 6 from 6 to 1,000,000.
"""

for i in range(6, 1000001, 6):
    print(i)
/python/python_fundamentals/for_loop_basic8.py
"""
Write a python program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
    sum += i
print(sum)

# or

a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in range(len(a)):
    sum += a[i]
print(sum)

# or

a = [1, 2, 5, 10, 255, 3]
sum