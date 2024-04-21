"""
Write a function to add the given tuple to the given list.
assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
"""

def add_tuple(list, tuple):
    list.extend(tuple)
    return list

print(add_tuple([5, 6, 7], (9, 10)))
<file_sep>/python/python_fundamentals/for_loop_basic_1.py
"""
Basic - Print all integers from 0 to 150.
"""

for i in range(0, 151):
    print(i)

"""
Basic - Print all the multiples of 5 from 5 to 1,000
"""

for i in range(5, 1001, 5):
    print(i)

"""
Basic - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
"""

for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

"""
Basic - Add odd integers from 0 to 500,000, and print the final sum.
"""

sum = 0
for i in range(0, 500001, 2):
    sum += i
print(sum)

"""
Basic - Print positive numbers starting at 2018, counting down by fours.
"""

for i in range(2018, 0, -4):
    print(i)

"""
Basic - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
"""

lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)
<file_sep>/python/python_fundamentals/functions_intermediate_1.py
"""
Intermediate - Update Values in Dictionaries and Lists
"""

x = [ [5,2,3], [10,8,9] ]
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
   'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

"""
Intermediate - Iterate Through a List of Dictionaries
"""

def iterateDictionary(list):
    for i in list:
        print(f"{i['first_name']} {i['last_name']}")

iterateDictionary(students)

"""
Intermediate - Iterate Through a Dictionary with List Values
"""

def iterateDictionaryWithListValues(dict):
    for key, value in dict.items():
        print(f"{key} :")
        for i in value:
            print(f"\t{i}")

iterateDictionaryWithListValues(sports_directory)

"""
Intermediate - Iterate Through a Dictionary with Dictionary