"""
The input is given as - a dictionary with a student name as a key and a tuple of float (student_height, student_weight) as a value, - minimal height, - minimal weight. Write a function to filter students that have height and weight above the minimum.
assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)=={'Cierra Vega': (6.2, 70)}
"""

def filter_data(data, min_height, min_weight):
    return {k:v for k,v in data.items() if v[0] > min_height and v[1] > min_weight}

print(filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70))
/python_basics/week_1/day_1/task_1.py
"""
Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
"""

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
/python_basics/week_1/day_2/task_1.py
"""
Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
"""

n = int(input("Enter a number: "))

sum = 0

for i in range(1, n+1):
    sum += i

print(sum)
/python_basics/week_1/day_2/task_2.py
"""
Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n.
"""

n = int(input("Enter a number: "))

choice = input("Enter's' for sum or 'p' for product: ")

sum = 0
product = 1

for i in range(1, n+1):
    if choice =='s':
        sum += i
    elif choice == 'p':
        product *= i

if choice =='s':
    print(sum)
elif choice == 'p':
    print(product)
/python_basics/week_1/day_2/task_3.py
"""
Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n.
"""

n = int(input("Enter a number: "))

choice = input("Enter's' for sum or 'p' for product: ")

sum = 0
product = 1

for i in range(1, n+1):
    if choice =='s':
        sum += i
    elif choice == 'p':
        product *= i

if choice =='s':
    print(sum)
elif choice == 'p':
    print(product)
/python_basics/week_1/day_1/task_2.py
"""
Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
"""

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print