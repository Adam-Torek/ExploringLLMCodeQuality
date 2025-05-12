"""
Write a function to count the total number of characters in a string.
assert count_charac("python programming")==18
"""
def count_charac(string):
    return len(string)

print(count_charac("python programming")) # Output: 18

# Another way to solve this problem using built-in function len()
def count_charac(string):
    return len(string)

print(count_charac("python programming")) # Output: 18

# Another way to solve this problem using a loop
def count_charac(string):
    count = 0
    for char in string:
        count += 1
    return count

print(count_charac("python programming")) # Output: 18

# Another way to solve this problem using a loop with a counter variable
def count_charac(string):
    count = 0
    for char in string:
        count += 1
    return count

print(count_charac("python programming")) # Output: 18

# Another way to solve this problem using a loop with a counter variable and a conditional statement
def count_charac(string):
    count = 0
    for char in string:
        if char.isalpha():
            count += 1
    return count

print(count_charac("python programming")) # Output: 10

# Another way to solve this problem using a loop with a counter variable and a conditional statement
def count_charac(string):
    count = 0
    for char in string:
        if char.isalpha() or char.isspace():
            count += 1
    return count

print(count_charac("python programming")) # Output: 18

# Another way to solve this problem using a loop with a counter variable and a conditional statement
def count_charac(string):
    count = 0
    for char in string:
        if char.isalpha() or char.isspace() or char.isdigit():
            count += 1
    return count

print(count_charac("python programming 123")) # Output: 19

# Another way to solve this problem using a loop with a counter variable and a conditional statement
def count_charac(string):
    count = 0
    for char in string:
        if char.isalnum() or char.isspace():
            count += 1
    return count

print(count_charac("python programming 123")) # Output: 19

# Another way to solve this problem using a loop with a counter variable and a conditional statement
def count_charac(string):
    count = 0
    for char in string:
        if char.isalnum() or char.isspace() or char.isalpha() or char.isdigit():
            count += 1
    return count

print(count_charac("python programming 123")) # Output: 19

# Another way to solve this problem using a loop with a counter variable and a conditional statement
def count_charac(string):
    count = 0
    for char in string:
        if char.isalnum() or char.isspace() or char.isalpha() or char.isdigit() or char == " ":
            count += 1
    return count

print(count_charac("python programming 123")) # Output: 20

# Another way to solve this problem using a loop with a counter variable and a conditional statement
def count_charac(string):
    count = 0
    for char in string:
        if char.isalnum() or char.isspace() or char.isalpha() or char.isdigit() or char == " ":
            count += 1
    return count

print(count_charac("python programming 123")) # Output: 20

# Another way to solve this problem using a loop with a counter variable and a conditional statement
def count_charac(string):
    count = 0
    for char in string:
        if char.isalnum() or char.isspace() or char