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
print(split_string('ab')) # Output: ['a', 'b']
print(split_string('abc')) # Output: ['a', 'b', 'c']
print(split_string('abcd')) # Output: ['a', 'b', 'c', 'd']
print(split_string('abcde')) # Output: ['a', 'b', 'c', 'd', 'e']
print(split_string('abcdef')) # Output: ['a', 'b', 'c', 'd', 'e', 'f']
print(split_string('abcdefg')) # Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(split_string('abcdefgh')) # Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(split_string('abcdefghi')) # Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(split_string('abcdefghij')) # Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(split_string('abcdefghijk')) # Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
print(split_string('abcdefghijkl')) # Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
print(split_string('abcdefghijklm')) # Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
print(split_string('abcdefghijklmn')) # Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
print(split_string('abcdefghijklmno')) # Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
print(split_string('abcdefghijklmnop')) # Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
print(split_string('abcdefghijklmnopq')) # Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q']
print(split_string('abcdefghijklmnopqr')) # Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r']
print(split_string('abcdefghijklmnopqrs')) # Output: ['a',