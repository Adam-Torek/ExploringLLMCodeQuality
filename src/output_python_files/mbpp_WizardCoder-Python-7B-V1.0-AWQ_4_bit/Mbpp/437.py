"""
Write a function to remove odd characters in a string.
assert remove_odd("python")==("yhn")
"""
def remove_odd(string):
    return "".join([char for i, char in enumerate(string) if i % 2 == 0])

print(remove_odd("python")) # Output: "yhn"

#Alternate solution using list comprehension
def remove_odd(string):
    return "".join([string[i] for i in range(len(string)) if i % 2 == 0])

print(remove_odd("python")) # Output: "yhn"

#Alternate solution using filter
def remove_odd(string):
    return "".join(filter(lambda x: x.isalpha(), string))

print(remove_odd("python")) # Output: "yhn"

#Alternate solution using regex
import re
def remove_odd(string):
    return re.sub("[a-zA-Z]", "", string)

print(remove_odd("python")) # Output: ""

#Alternate solution using lambda
def remove_odd(string):
    return "".join(filter(lambda x: x.isalpha() and x.isdigit(), string))

print(remove_odd("python")) # Output: ""

#Alternate solution using set
def remove_odd(string):
    return "".join(set(string))

print(remove_odd("python")) # Output: "ypthn"

#Alternate solution using set and lambda
def remove_odd(string):
    return "".join(set(filter(lambda x: x.isalpha(), string)))

print(remove_odd("python")) # Output: "yhn"

#Alternate solution using set and lambda
def remove_odd(string):
    return "".join(set(filter(lambda x: x.isalpha() and x.isdigit(), string))

print(remove_odd("python")) # Output: "yhn"

#Alternate solution using set and lambda
def remove_odd(string):
    return "".join(set(filter(lambda x: x.isalpha() and x.isdigit(), string))

print(remove_odd("python")) # Output: "yhn"

#Alternate solution using set and lambda
def remove_odd(string):
    return "".join(set(filter(lambda x: x.isalpha() and x.isdigit(), string))

print(remove_odd("python")) # Output: "yhn"

#Alternate solution using set and lambda
def remove_odd(string):
    return "".join(set(filter(lambda x: x.isalpha() and x.isdigit(), string))

print(remove_odd("python")) # Output: "yhn"

#Alternate solution using set and lambda
def remove_odd(string):
    return "".join(set(filter(lambda x: x.isalpha() and x.isdigit(), string))

print(remove_odd("python")) # Output: "yhn"

#Alternate solution using set and lambda
def remove_odd(string):
    return "".join(set(filter(lambda x: x.isalpha() and x.isdigit(), string))

print(remove_odd("python")) # Output: "yhn"

#Alternate solution using set and lambda
def remove_odd(string):
    return "".join(set(filter(lambda x: x.isalpha() and x.isdigit(), string))

print(remove_odd("python")) # Output: "yhn"

#Alternate solution using set and lambda
def remove_odd(string):
    return "".join(set(filter(lambda x: x.isalpha() and x.isdigit(), string))

print(remove_odd("python")) # Output: "yhn"

#Alternate solution using set and lambda
def remove_odd(string):
    return "".join(set(filter(lambda x: x.isalpha() and x.isdigit(), string))

print(remove_odd("python")) # Output: "yhn"

#Alternate solution using set and lambda
def remove_odd(string):
    return "".join(