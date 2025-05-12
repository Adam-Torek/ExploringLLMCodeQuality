"""
Write a function to check if the given tuples contain the k or not.
assert check_K((10, 4, 5, 6, 8), 6) == True
"""

def check_K(tup, k):
    for i in tup:
        if i == k:
            return True
    return False

print(check_K((10, 4, 5, 6, 8), 6))
/python_basics/01_python_basics/02_variables_and_data_types/01_variables.py
"""
Write a program that asks the user for their name and greets them with their name.
"""

name = input("What is your name? ")
print("Hello, " + name)
/python_basics/01_python_basics/02_variables_and_data_types/03_data_types.py
"""
Write a program that asks the user for their name and greets them with their name.
"""

name = input("What is your name? ")
print("Hello, " + name)

# Write a program that asks the user for their name and greets them with their name.
# If the name is longer than 4 characters, print "Hello, " + name.
# If the name is shorter than 4 characters, print "Hello, " + name + "!".

name = input("What is your name? ")
if len(name) > 4:
    print("Hello, " + name)
else:
    print("Hello, " + name + "!")
/python_basics/01_python_basics/03_conditional_statements/02_if_else.py
"""
Write a program that asks the user for their name and greets them with their name.
If the name is longer than 4 characters, print "Hello, " + name.
If the name is shorter than 4 characters, print "Hello, " + name + "!".
"""

name = input("What is your name? ")
if len(name) > 4:
    print("Hello, " + name)
else:
    print("Hello, " + name + "!")

# Write a program that asks the user for their name and greets them with their name.
# If the name is longer than 4 characters, print "Hello, " + name.
# If the name is shorter than 4 characters, print "Hello, " + name + "!".
# If the name is exactly 4 characters long, print "Hello, " + name + "!".

name = input("What is your name? ")
if len(name) > 4:
    print("Hello, " + name)
elif len(name) < 4:
    print("Hello, " + name + "!")
else:
    print("Hello, " + name + "!")
/python_basics/01_python_basics/03_conditional_statements/03_if_elif_else.py
"""
Write a program that asks the user for their name and greets them with their name.
If the name is longer than 4 characters, print "Hello, " + name.
If the name is shorter than 4 characters, print "Hello, " + name + "!".
If the name is exactly 4 characters long, print "Hello, " + name + "!".
"""

name = input("What is your name? ")
if len(name) > 4:
    print("Hello, " + name)
elif len(name) < 4:
    print("Hello, " + name + "!")
else:
    print("Hello, " + name + "!")

# Write a program that asks the user for their name and greets them with their name.
# If the name is longer than 4 characters, print "Hello, " + name.
# If the name is shorter than 4 characters, print "Hello, " + name + "!".
# If the name is exactly 4 characters long, print "Hello, " + name + "!".
# If the name is exactly 5 characters long, print "Hello, " + name + "!".

name = input("What is your name? ")
if len(name) > 4:
    print("Hello, " + name)
elif len(name) < 4:
    print("Hello, " + name + "!")
elif len(name) == 4:
    print("Hello, " + name + "!")
else:
    print("Hello, "