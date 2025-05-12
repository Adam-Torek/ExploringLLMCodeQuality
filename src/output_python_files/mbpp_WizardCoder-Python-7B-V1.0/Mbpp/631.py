"""
Write a function to replace whitespaces with an underscore and vice versa in a given string.
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
"""

def replace_spaces(string):
    return string.replace(" ", "_")

#Alternative solution
def replace_spaces(string):
    return string.replace(" ", "_")

#Test cases
print(replace_spaces('Jumanji The Jungle')) # Output: Jumanji_The_Jungle
print(replace_spaces('Hello World')) # Output: Hello_World
print(replace_spaces('Python is awesome')) # Output: Python_is_awesome
print(replace_spaces('I love Python')) # Output: I_love_Python
print(replace_spaces('I love Python programming')) # Output: I_love_Python_programming
print(replace_spaces('I love Python programming in Python')) # Output: I_love_Python_programming_in_Python