"""
Write a function to find the union of the elements of two given tuples and output them in sorted order.
assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)
"""

def union_elements(tuple1, tuple2):
    return sorted(set(tuple1 + tuple2))

print(union_elements((3, 4, 5, 6),(5, 7, 4, 10) ))
<file_sep>/python_basics/02_variables_and_types/02_variables_and_types.py
"""
Write a program that asks the user for their name and greets them with their name.
"""

name = input("What is your name? ")
print("Hello " + name)

"""
Write a program that asks the user for their name and greets them with their name.
If the length of their name is less than 3, print their name and a message about being a short name.
"""

name = input("What is your name? ")
if len(name) < 3:
    print("Your name is " + name + " and it is a short name")
else:
    print("Hello " + name)

"""
Write a program that asks the user for their name and greets them with their name.
If the length of their name is less than 3, print their name and a message about being a short name.
If the length of their name is greater than or equal to 3, ask them for their age and print their name and age.
"""

name = input("What is your name? ")
if len(name) < 3:
    print("Your name is " + name + " and it is a short name")
else:
    age = input("What is your age? ")
    print("Hello " + name + " and you are " + age + " years old")

"""
Write a program that asks the user for their name and greets them with their name.
If the length of their name is less than 3, print their name and a message about being a short name.
If the length of their name is greater than or equal to 3, ask them for their age and print their name and age.
If they are under 13 years old, print a message about being a child.
"""

name = input("What is your name? ")
if len(name) < 3:
    print("Your name is " + name + " and it is a short name")
else:
    age = input("What is your age? ")
    if int(age) < 13:
        print("Hello " + name + " and you are " + age + " years old and you are a child")
    else:
        print("Hello " + name + " and you are " + age + " years old")

"""
Write a program that asks the user for their name and greets them with their name.
If the length of their name is less than 3, print their name and a message about being a short name.
If the length of their name is greater than or equal to 3, ask them for their age and print their name and age.
If they are under 13 years old, print a message about being a child.
If they are equal to or over 13 years old, print a message about being an adult.
"""

name = input("What is your name? ")
if len(name) < 3:
    print("Your name is " + name + " and it is a short name")
else:
    age = input("What is your age? ")
    if int(age) < 13:
        print("Hello " + name + " and you are " + age + " years old and you are a child")
    elif int(age) >= 13:
        print("Hello " + name + " and you are " + age + " years old and you are an adult")

"""
Write a program that asks the user for their name and greets them with their name.
If the length of their name is less than 3, print their name and a message about being a short name.
If the length of their name is greater than or equal to 3, ask them for their age and print their name and age.
If they are under 13 years old, print a message about being a child.
If they are equal to or over 13 years old, print a message about being an adult.