"""
Write a function to remove uppercase substrings from a given string.
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
"""

def remove_uppercase(string):
    return ''.join([char for char in string if char.islower()])

# Test the function
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'<|endoftext|>