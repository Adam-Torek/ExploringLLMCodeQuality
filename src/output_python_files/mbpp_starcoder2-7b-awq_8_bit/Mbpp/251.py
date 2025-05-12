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
Basic 13

Print integers from 0 to 1000.
Print all the integers from 1 to 1000000.
Print all the multiples of 5 from 5 to 1,000,000.
Print integers 1 to 100,000.
Print the numbers from -10 to 10,000.
Print the numbers between -10 and 10.
Print the multiples of 3 from -10 to 1000.
Print the multiples of 5 from -10 to 1000.
Print the multiples of 7 from -10 to 11000.
Print the multiples of 10 from -10 to 11000.
Print integers 1 to 100,000,000.
Print the multiples of 11 from -10 to 11000000.
Print the multiples of 13 from -10 to 11000000.
Print the multiples of 17 from -10 to 11000000.
"""

# Print integers from 0 to 1000.
for i in range(1001):
    print(i)

# Print all the integers from 1 to 1000000.
for i in range(1, 1000001):
    print(i)

# Print all the multiples of 5 from 5 to 1,000,000.
for i in range(5, 1000001, 5):
    print(i)

# Print integers 1 to 100,000.
for i in range(1, 100001):
    print(i)

# Print the numbers from -10 to 10,000.
for i in range(-10000, 10001):
    print(i)

# Print the numbers between -10 and 10.
for i in range(-10, 11):
    print(i)

# Print the multiples of 3 from -10 to 1000.
for i in range(-10, 1001, 3):
    print(i)

# Print the multiples of 5 from -10 to 1000.
for i in range(-10, 1001, 5):
    print(i)

# Print the multiples of 7 from -10 to 11000.
for i in range(-10, 11001, 7):
    print(i)

# Print the multiples of 10 from -10 to 11000.
for i in range(-10, 11001, 10):
    print(i)

# Print integers 1 to 100,000,000.
for i in range(1, 100000001):
    print(i)

# Print the multiples of 11 from -10 to 11000000.
for i in range(-10, 11000001, 11):
    print(i)

# Print the multiples of 13 from -10 to 11000000.
for i in range(-10, 11000001, 13):
    print(i)

# Print the multiples of 17 from -1