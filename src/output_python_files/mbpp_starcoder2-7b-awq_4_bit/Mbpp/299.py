"""
Write a function to calculate the maximum aggregate from the list of tuples.
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
"""

def max_aggregate(list_of_tuples):
    max_tuple = list_of_tuples[0]
    for tuple in list_of_tuples:
        if tuple[1] > max_tuple[1]:
            max_tuple = tuple
    return max_tuple

assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
/python/python_fundamentals/for_loop_basic2.py
"""
Basic - Print all integers from 0 to 150.

Print all the multiples of 5 from 5 to 1,000

Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

Print the sum of all integers from 0 to 5000.

Print all the multiples of 6 up to 60,000,000 (give or take).

Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

Print the sum of all multiples of 3 and 5 up to 1,000.

"""

# Basic - Print all integers from 0 to 150.
for i in range(151):
    print(i)

# Print all the multiples of 5 from 5 to 1,000
for i in range(5, 1001, 5):
    print(i)

# Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(1, 101):
    if i % 5 == 0 and i % 10!= 0:
        print("Coding")
    elif i % 10 == 0:
        print("Coding Dojo")
    else:
        print(i)

# Print the sum of all integers from 0 to 5000.
sum = 0
for i in range(5001):
    sum += i
print(sum)

# Print all the multiples of 6 up to 60,000,000 (give or take).
for i in range(6, 60000001, 6):
    print(i)

# Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(1, 101):
    if i % 5 == 0 and i % 10!= 0:
        print("Coding")
    elif i % 10 == 0:
        print("Coding Dojo")
    else:
        print(i)

# Print the sum of all multiples of 3 and 5 up to 1,000.
sum = 0
for i in range(1, 1001):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(sum)
/python/python_fundamentals/for_loop_basic1.py
"""
Basic - Print all the numbers from 0 to 100.

Print all the even numbers from 10 to 1000.

Print all the odd numbers from 1 to 1000.

Print all the multiples of 5 from 5 to 1,000.

Print the sum of all the values from 0 to 10