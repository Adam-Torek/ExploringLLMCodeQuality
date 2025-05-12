"""
Write a function to extract values between quotation marks from a string.
assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
"""

def extract_values(string):
    return [x[1:-1] for x in string.split(',')]

print(extract_values('"Python", "PHP", "Java"'))
/python/python_fundamentals/for_loop_basic2.py
"""
Print integers from 0 to 100.
Print all the even numbers from 1 to 1000.
Print all the odd numbers from 1 to 1000.
Print all the multiples of 5 from 5 to 1,000,000.
Print integers 1 to 100. If even, print "even" instead. If odd, print "odd".
Print the sum of all the values from 0 to 1000.
Print positive numbers starting at 2018, counting down by 4.
Print multiples of 5 from -10 to 100.
Print the sum of all the values from -10 to 100.
Print integers from 2000 to 2018. Print back 1989 instead of 2018 if the value is a leap year.
"""

for i in range(0, 101):
    print(i)

for i in range(1, 1001):
    if i % 2 == 0:
        print(i)

for i in range(1, 1001):
    if i % 2!= 0:
        print(i)

for i in range(5, 1000001):
    if i % 5 == 0:
        print(i)

for i in range(1, 101):
    if i % 2 == 0:
        print("even")
    else:
        print("odd")

sum = 0
for i in range(0, 1001):
    sum += i
print(sum)

for i in range(2018, 0, -4):
    print(i)

for i in range(-10, 101):
    if i % 5 == 0:
        print(i)

sum = 0
for i in range(-10, 101):
    sum += i
print(sum)

for i in range(2000, 2019):
    if i % 4 == 0:
        print(i)
    else:
        print(1989)
/python/python_fundamentals/for_loop_basic1.py
"""
Print all integers from 0 to 150.
Print all the multiples of 5 from 5 to 1,000.
Print integers 1 to 100. If even, print "even" instead. If odd, print "odd".
Print the sum of all the values from 0 to 1000.
Print positive numbers starting at 2018, counting down by 4.
Print multiples of 5 from -10 to 100.
Print the sum of all the values from -10 to 100.
Print integers from 2000 to 2018. Print back 1989 instead of 2018 if the value is a leap year.
"""

for i in range(0, 151):
    print(i)

for i in range(5, 1000):
    if i % 5 == 0:
        print(i)

for i in range(1, 101):
    if i % 2 == 0:
        print("even")
    else:
        print("odd")

sum = 0
for i in range(0, 1001):
    sum += i
print(sum)

for i in range(2018, 0, -4):
    print(i)

for i in range(-10, 101):
    if i % 5 == 0:
        print(i)

sum = 0
for i in range(-10,