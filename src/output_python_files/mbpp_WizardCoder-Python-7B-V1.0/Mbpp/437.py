"""
Write a function to remove odd characters in a string.
assert remove_odd("python")==("yhn")
"""
def remove_odd(string):
    return "".join([char for char in string if char.isalpha() and char.lower() not in "aeiou"])

print(remove_odd("python"))

#Alternate solution:
def remove_odd(string):
    return "".join([char for char in string if char.isalpha() and char.lower() not in "aeiouAEIOU"])

print(remove_odd("python"))

#Alternate solution:
def remove_odd(string):
    return "".join([char for char in string if char.isalpha() and char.lower() not in "aeiou"])

print(remove_odd("python"))

#Alternate solution:
def remove_odd(string):
    return "".join(filter(lambda char: char.isalpha() and char.lower() not in "aeiou", string))

print(remove_odd("python"))

#Alternate solution:
def remove_odd(string):
    return "".join(char for char in string if char.isalpha() and char.lower() not in "aeiou")

print(remove_odd("python"))

#Alternate solution:
def remove_odd(string):
    return "".join(char for char in string if char.isalpha() and char not in "AEIOUaeiou")

print(remove_odd("python"))

#Alternate solution:
def remove_odd(string):
    return "".join(char for char in string if char.isalpha() and char.lower() not in "aeiou")

print(remove_odd("python"))

#Alternate solution:
def remove_odd(string):
    return "".join(char for char in string if char.isalpha() and char not in "AEIOU")

print(remove_odd("python"))

#Alternate solution:
def remove_odd(string):
    return "".join(char for char in string if char.isalpha() and char.lower() not in "aeiou")

print(remove_odd("python"))

#Alternate solution:
def remove_odd(string):
    return "".join(char for char in string if char.isalpha() and char not in "AEIOU")

print(remove_odd("python"))

#Alternate solution:
def remove_odd(string):
    return "".join(char for char in string if char.isalpha() and char.lower() not in "aeiou")

print(remove_odd("python"))

#Alternate solution:
def remove_odd(string):
    return "".join(char for char in string if char.isalpha() and char.lower() not in "AEIOU")

print(remove_odd("python"))

#Alternate solution:
def remove_odd(string):
    return "".join(char for char in string if char.isalpha() and char not in "AEIOUaeiou")

print(remove_odd("python"))

#Alternate solution:
def remove_odd(string):
    return "".join(char for char in string if char.isalpha() and char.lower() not in "AEIOU")

print(remove_odd("python"))

#Alternate solution:
def remove_odd(string):
    return "".join(char for char in string if char.isalpha() and char not in "AEIOU")

print(remove_odd("python"))

#Alternate solution:
def remove_odd(string):
    return "".join(char for char in string if char.isalpha() and char.lower() not in "AEIOU")

print(remove_odd("python"))

#Alternate solution:
def remove_odd(string):
    return "".join(char for char in string if char.isalpha() and char not in "aeiou")

print(remove_odd("python"))

#Alternate solution:
def remove_odd(string):
    return "".join(char for char in string if char.isalpha() and char.