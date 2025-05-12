"""
Write a function that takes in a list and an element and inserts the element before each element in the list, and returns the resulting list.
assert insert_element(['Red', 'Green', 'Black'],'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']
"""

def insert_element(list, element):
    new_list = []
    for i in range(len(list)):
        new_list.append(element)
        new_list.append(list[i])
    return new_list

print(insert_element(['Red', 'Green', 'Black'], 'c'))
/python/python_fundamentals/for_loop_basic2.py
"""
Basic 13: For Loops
"""

# 1. Basic
for i in range(1, 1001):
    print(i)

# 2. Multiples of Five
for i in range(5, 1000000, 5):
    print(i)

# 3. Counting, the Dojo Way
for i in range(1, 100):
    if i % 5 == 0:
        print("Coding")
    elif i % 10 == 0:
        print("Coding Dojo")
    else:
        print(i)

# 4. Whoa. That Sucker's Huge
sum = 0
for i in range(1, 500000):
    if i % 2 == 1:
        sum += i
print(sum)

# 5. Countdown by Fours
for i in range(2018, 0, -4):
    print(i)

# 6. Flexible Counter
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)
/python/python_fundamentals/for_loop_basic1.py
"""
Basic 12: For Loops
"""

# 1. Basic
for i in range(1, 10):
    print(i)

# 2. Multiples of Three
for i in range(3, 1000, 3):
    print(i)

# 3. Counting, the Dojo Way
for i in range(1, 100):
    if i % 5 == 0:
        print("Coding")
    else:
        print(i)

# 4. Whoa. That Sucker's Huge
sum = 0
for i in range(1, 500000):
    sum += i
print(sum)

# 5. Countdown by Fours
for i in range(2018, 0, -4):
    print(i)

# 6. Flexible Counter
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)
/python/python_fundamentals/functions_intermediate1.py
"""
Intermediate 1: Functions
"""

# 1. Countdown
def countdown(num):
    for i in range(num, -1, -1):
        print(i)

countdown(10)

# 2. Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]

print_and_return([1, 2])

# 3. First Plus Length
def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([1, 2, 3, 4, 5]))

# 4. Values Greater than Second
def values_greater_than_second(list):
    new_list = []
    for i in range(len(list)):
        if list[i] > list[1]:
            new_list.append(list[i])
    if len(new_list) == 0:
        return False
    else:
        return new_list

print(values_greater_than_second([5, 2, 3, 2, 1, 4]))

# 5. This Length, That Value
def length_and_value(size, value