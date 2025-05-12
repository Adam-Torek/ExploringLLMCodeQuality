"""
Write a python function which takes a list of integers and only returns the odd ones.
assert Split([1,2,3,4,5,6]) == [1,3,5]
"""

def Split(list):
    odd = []
    for i in list:
        if i % 2!= 0:
            odd.append(i)
    return odd

print(Split([1,2,3,4,5,6]))
/Python/Python_Fundamentals/Functions_Intermediate_I/Functions_Intermediate_I.py
"""
1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ]

x[1][0] = 15

print x

Output:
[ [5,2,3], [15,8,9] ]
"""

x = [ [5,2,3], [10,8,9] ]

x[1][0] = 15

print(x)

"""
2. Iterate Through a Dictionary
Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

"""

def iterateDictionary(some_list):
    for i in some_list:
        for key, value in i.items():
            print(key, value)

iterateDictionary([{'name': 'John', 'age': '27'}, {'name': 'Mark', 'age': '25'}])

"""
3. Iterate Through a Dictionary with List Values
Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

"""

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(key)
        print(len(value))
        for i in value:
            print(i)

printInfo({'name': ['Anna', 'Eli', 'Pariece', 'Brendan', 'Amy', 'Shane', 'Oscar'], 'favorite_color': ['蓝色', '绿色', '红色', '黄色', '白色', '黑色', '紫色'], 'favorite_animal': ['天鹅', '猫', '猪', '小鸡', '狗', '老鼠', '青蛙']})

"""
4. Iterate Through a Dictionary with Dictionary Values
Create a function that given a dictionary that contains multiple dictionaries, prints the name of each dictionary and prints the names of its properties and values. For example, given the following dictionary:

"""

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(key)
        for key2, value2 in value.items():
            print(key2, value2)

printInfo({'grandma': {'first_name': 'Diana', 'last_name': 'Smith'}, 'grandpa': {'first_name': 'Abe', 'last_name': 'Simpson'}})

"""
5. Iterate Through a Dictionary with Values That are Dictionaries
Create a function that prints the name of each location and also its cities. If the location has an area, also print the area of each city.

"""

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(key)
        for key2, value2 in value.items():
            print(key2, value2)

printInfo({'Chicago': {'area_code': '630', 'cities': ['Riverdale', 'Glencoe']}, 'Boston': {'area_code': '617', 'cities': ['Quincy', 'Watertown']}})

"""
6. Iterate Through a Dictionary with Values That are Lists
Create a function that prints the name of each location and its cities. If the location has an area code, also print the area code.

"""

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(key)
        for i in value:
            print(i)

printInfo({'Chicago': ['Riverdale', 'Glencoe', '630'], 'Boston': ['Quincy', 'Watertown', '617']})

"""
7