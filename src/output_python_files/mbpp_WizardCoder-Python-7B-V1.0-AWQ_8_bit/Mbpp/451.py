"""
Write a function to remove all whitespaces from the given string.
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
"""

def remove_whitespaces(string):
    return ''.join(string.split())

# Test cases
print(remove_whitespaces(' Google    Flutter ')) # Output: 'GoogleFlutter'
print(remove_whitespaces(' Hello World ') # Output: 'HelloWorld'
print(remove_whitespaces(' Python is awesome ')) # Output: 'Pythonisawesome'
print(remove_whitespaces(' I love Python ')) # Output: 'IlovePython'
print(remove_whitespaces(' I love Python programming ')) # Output: 'IlovePythonprogramming'
print(remove_whitespaces(' I love Python programming! ')) # Output: 'IlovePythonprogramming!'
print(remove_whitespaces('')) # Output: ''
print(remove_whitespaces(' ')) # Output: ''
print(remove_whitespaces('     ')) # Output: ''
print(remove_whitespaces('')) # Output: ''