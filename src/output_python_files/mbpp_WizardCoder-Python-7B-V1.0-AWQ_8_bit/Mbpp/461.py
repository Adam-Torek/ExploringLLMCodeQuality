"""
Write a python function to count the upper case characters in a given string.
assert upper_ctr('PYthon') == 1
"""
def upper_ctr(string):
    count = 0
    for i in string:
        if i.isupper():
            count += 1
    return count

print(upper_ctr('PYthon')) # Output: 1
print(upper_ctr('Python')) # Output: 0
print(upper_ctr('Hello World')) # Output: 2
print(upper_ctr('AaBbCc')) # Output: 0
print(upper_ctr('aBcDeFg')) # Output: 3
print(upper_ctr('')) # Output: 0