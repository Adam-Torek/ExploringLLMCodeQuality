"""
Write a python function which takes a list and returns a list with the same elements, but the k'th element removed.
assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
"""

def remove_kth_element(list,k):
    return list[:k-1]+list[k:]

print(remove_kth_element([1,1,2,3,4,4,5,1],3))
/python/python_basics/01_hello_world.py
"""
Write a python program which prints "Hello World"
"""

print("Hello World")
/python/python_basics/03_print_numbers.py
"""
Write a python program which prints the numbers from 0 to 9
"""

for i in range(10):
    print(i)
/python/python_basics/02_print_hello_world_10_times.py
"""
Write a python program which prints "Hello World" 10 times
"""

for i in range(10):
    print("Hello World")
/python/python_basics/04_print_odd_numbers.py
"""
Write a python program which prints the odd numbers from 0 to 9
"""

for i in range(10):
    if i%2==1:
        print(i)
/python/python_basics/05_print_even_numbers.py
"""
Write a python program which prints the even numbers from 0 to 9
"""

for i in range(10):
    if i%2==0:
        print(i)
/python/python_basics/06_print_even_numbers_between_0_and_100.py
"""
Write a python program which prints the even numbers from 0 to 100
"""

for i in range(101):
    if i%2==0:
        print(i)
/python/python_basics/07_print_odd_numbers_between_0_and_100.py
"""
Write a python program which prints the odd numbers from 0 to 100
"""

for i in range(101):
    if i%2==1:
        print(i)
/python/python_basics/08_print_numbers_between_0_and_100_with_step_5.py
"""
Write a python program which prints the numbers from 0 to 100 with step 5
"""

for i in range(0,101,5):
    print(i)
/python/python_basics/09_print_numbers_between_0_and_100_with_step_3.py
"""
Write a python program which prints the numbers from 0 to 100 with step 3
"""

for i in range(0,101,3):
    print(i)
/python/python_basics/10_print_numbers_between_0_and_100_with_step_7.py
"""
Write a python program which prints the numbers from 0 to 100 with step 7
"""

for i in range(0,101,7):
    print(i)
/python/python_basics/11_print_numbers_between_0_and_100_with_step_2.py
"""
Write a python program which prints the numbers from 0 to 100 with step 2
"""

for i in range(0,101,2):
    print(i)