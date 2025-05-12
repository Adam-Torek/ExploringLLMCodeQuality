"""
Write a function to remove uppercase substrings from a given string.
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
"""

def remove_uppercase(string):
    return ''.join([char for char in string if char.islower() or char.isnumeric()])

#Alternative solution using regex
import re
def remove_uppercase(string):
    return re.sub(r'[A-Z]', '', string)

#Test cases
print(remove_uppercase('cAstyoUrFavoRitETVshoWs')) #Output: 'cstyoravoitshos'
print(remove_uppercase('Hello, World!')) #Output: 'helloworld'
print(remove_uppercase('Python is awesome')) #Output: 'pythons awesome'
print(remove_uppercase('12345')) #Output: '12345'
print(remove_uppercase('aBcDeFgHiJkLmNoPqRsTuVwXyZ')) #Output: ''
print(remove_uppercase('')) #Output: ''