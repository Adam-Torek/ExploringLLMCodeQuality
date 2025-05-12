"""
Write a function to remove uppercase substrings from a given string.
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
"""

def remove_uppercase(string):
    return ''.join([char for char in string if char.islower() or char.isdigit() or char.isspace()])

print(remove_uppercase('cAstyoUrFavoRitETVshoWs')) # Output: 'cstyoravoitshos'

# Another solution:
def remove_uppercase(string):
    return ''.join([char for char in string if not char.isupper()])

print(remove_uppercase('cAstyoUrFavoRitETVshoWs')) # Output: 'cstyoravoitshos'