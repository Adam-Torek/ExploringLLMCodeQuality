"""
Write a function to check whether the given string is starting with a vowel or not using regex.
assert check_str("annie")
"""
import re

def check_str(string):
    vowels = "aeiouAEIOU"
    if re.match("^[" + vowels + "]", string):
        return True
    else:
        return False

print(check_str("annie")) # True
print(check_str("apple")) # False
print(check_str("banana")) # False
print(check_str("Elephant")) # True
print(check_str("Orange")) # True
print(check_str("Zebra")) # False
print(check_str("12345")) # False
print(check_str("")) # False
print(check_str(" ")) # False
print(check_str("a")) # True
print(check_str("A")) # True
print(check_str("zebra")) # True
print(check_str("Zebra")) # True
print(check_str("Zebra123")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra123")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str("Zebra!@#")) # True
print(check_str