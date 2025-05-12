"""
Write a python function to split a string into characters.
assert split('python') == ['p','y','t','h','o','n']
"""
def split_string(string):
    return list(string)

# Test cases
print(split_string('python')) # Output: ['p', 'y', 't', 'h', 'o', 'n']
print(split_string('hello')) # Output: ['h', 'e', 'l', 'l', 'o']
print(split_string('world')) # Output: ['w', 'o', 'r', 'l', 'd']
print(split_string('programming')) # Output: ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
print(split_string('')) # Output: []
print(split_string('a')) # Output: ['a']
print(split_string('')) # Output: []

# Test cases with special characters
print(split_string('!@#$%^&*()')) # Output: ['!', '@', '#', '$', '%', '^', '&', '*', ')']
print(split_string('1234567890')) # Output: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
print(split_string('')) # Output: []
print(split_string('')) # Output: []

# Test cases with empty string
print(split_string('')) # Output: []
print(split_string('')) # Output: []

# Test cases with single character string
print(split_string('a')) # Output: ['a']
print(split_string('b')) # Output: ['b']
print(split_string('c')) # Output: ['c']
print(split_string('d')) # Output: ['d']
print(split_string('e')) # Output: ['e']
print(split_string('f')) # Output: ['f']
print(split_string('g')) # Output: ['g']
print(split_string('h')) # Output: ['h']
print(split_string('i')) # Output: ['i']
print(split_string('j')) # Output: ['j']
print(split_string('k')) # Output: ['k']
print(split_string('l')) # Output: ['l']
print(split_string('m')) # Output: ['m']
print(split_string('n')) # Output: ['n']
print(split_string('o')) # Output: ['o']
print(split_string('p')) # Output: ['p']
print(split_string('q')) # Output: ['q']
print(split_string('r')) # Output: ['r']
print(split_string('s')) # Output: ['s']
print(split_string('t')) # Output: ['t']
print(split_string('u')) # Output: ['u']
print(split_string('v')) # Output: ['v']
print(split_string('w')) # Output: ['w']
print(split_string('x')) # Output: ['x']
print(split_string('y')) # Output: ['y']
print(split_string('z')) # Output: ['z']

# Test cases with multiple character string
print(split_string('python')) # Output: ['p', 'y', 't', 'h', 'o', 'n']
print(split_string('hello')) # Output: ['h', 'e', 'l', 'l', 'o']
print(split_string('world')) # Output: ['w', 'o', 'r', 'l', 'd']
print(split_string('programming')) # Output: ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
print(split_string('!@#$%^&*()')) # Output: ['!', '@', '#', '$', '%', '^', '&', '*', ')']
print(split_string('1234567890')) # Output: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# Test cases with empty string
print(split