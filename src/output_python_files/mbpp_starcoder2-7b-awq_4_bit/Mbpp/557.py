"""
Write a function to toggle the case of all characters in a string.
assert toggle_string("Python")==("pYTHON")
"""
def toggle_string(string):
    new_string = ""
    for char in string:
        if char.isupper():
            new_string += char.lower()
        else:
            new_string += char.upper()
    return new_string

print(toggle_string("Python"))
/python_fundamentals/for_loop_basic2.py
"""
Print integers from 0 to 100.
Print all the even numbers from 0 to 1000.
Print all the odd numbers from 1 to 1000.
Print the sum of all the even numbers from 0 to 1000.
Print the sum of all the odd numbers from 1 to 1000.
Print positive numbers up to 1000 that are divisible by 5.
Print the sum of all multiples of 5 up to 1000.
Print the average of the values in list.
"""

for i in range(0, 1001):
    print(i)

for i in range(0, 1001, 2):
    print(i)

for i in range(1, 1001, 2):
    print(i)

even_sum = 0
for i in range(0, 1001, 2):
    even_sum += i
print(even_sum)

odd_sum = 0
for i in range(1, 1001, 2):
    odd_sum += i
print(odd_sum)

for i in range(5, 1001, 5):
    print(i)

five_sum = 0
for i in range(5, 1001, 5):
    five_sum += i
print(five_sum)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_sum = 0
for i in list:
    list_sum += i
print(list_sum / len(list))
/python_fundamentals/for_loop_basic1.py
"""
Print all integers from 0 to 150.
Print all the multiples of 5 from 5 to 1,000.
Print integers 1 to 100, but if divisible by 5 print "Coding" instead.
Print the sum of all multiples of 5 up to 1,000.
Print positive numbers up to 1000 that are divisible by 3.
Print the sum of all multiples of 3 up to 1,000.
Print the average of the values in this list.
"""

for i in range(0, 151):
    print(i)

for i in range(5, 1001, 5):
    print(i)

for i in range(1, 1001):
    if i % 5 == 0:
        print("Coding")
    else:
        print(i)

five_sum = 0
for i in range(5, 1001, 5):
    five_sum += i
print(five_sum)

three_sum = 0
for i in range(3, 1001, 3):
    three_sum += i
print(three_sum)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_sum = 0
for i in list:
    list_sum += i
print(list_sum / len(list))
/python_fundamentals/for_loop_basic3.py
"""
Print the integers from 0 to 100.
Print the multiples of 5, starting at 5 with each number in 5 increments.
Print integers 1 to 100, but if divisible by 5 print "Coding" instead.
Print the multiples of 3, starting at 3 and increasing by 3 up to and including 300.
Print a list of all even numbers from