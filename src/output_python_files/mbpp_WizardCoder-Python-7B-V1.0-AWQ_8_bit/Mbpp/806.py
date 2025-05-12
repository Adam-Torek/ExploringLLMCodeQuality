"""
Write a function to find maximum run of uppercase characters in the given string.
assert max_run_uppercase('GeMKSForGERksISBESt') == 5
"""

def max_run_uppercase(string):
    max_run = 0
    current_run = 0
    current_upper = 0
    for char in string:
        if char.isupper():
            current_run += 1
        else:
            if current_run > max_run:
                max_run = current_run
            current_run = 0
        if current_run > max_run:
            max_run = current_run
    return max_run

print(max_run_uppercase('GeMKSForGERksISBESt')) # Output: 5
print(max_run_uppercase('AABBBCCaDDD')) # Output: 3
print(max_run_uppercase('A')) # Output: 1
print(max_run_uppercase('a')) # Output: 0
print(max_run_uppercase('')) # Output: 0
print(max_run_uppercase('AaBbCc')) # Output: 0
print(max_run_uppercase('AAA')) # Output: 3
print(max_run_uppercase('AAAa')) # Output: 3
print(max_run_uppercase('AAAaA')) # Output: 3
print(max_run_uppercase('AaAaAaAa')) # Output: 3
print(max_run_uppercase('AaAaAaAaA')) # Output: 7
print(max_run_uppercase('AaAaAaAaAa')) # Output: 7
print(max_run_uppercase('AaAaAaAaAaA')) # Output: 8
print(max_run_uppercase('AaAaAaAaAaAa')) # Output: 9
print(max_run_uppercase('AaAaAaAaAaAaA')) # Output: 10
print(max_run_uppercase('AaAaAaAaAaAaAa')) # Output: 11
print(max_run_uppercase('AaAaAaAaAaAaAaA')) # Output: 12
print(max_run_uppercase('AaAaAaAaAaAaAaAa')) # Output: 13
print(max_run_uppercase('AaAaAaAaAaAaAaAaA')) # Output: 14
print(max_run_uppercase('AaAaAaAaAaAaAaAaAa')) # Output: 15
print(max_run_uppercase('AaAaAaAaAaAaAaAaAaA')) # Output: 16
print(max_run_uppercase('AaAaAaAaAaAaAaAaAaAa')) # Output: 17
print(max_run_uppercase('AaAaAaAaAaAaAaAaAaAaA')) # Output: 18
print(max_run_uppercase('AaAaAaAaAaAaAaAaAaAaAa')) # Output: 19
print(max_run_uppercase('AaAaAaAaAaAaAaAaAaAaAaA')) # Output: 20
print(max_run_uppercase('AaAaAaAaAaAaAaAaAaAaAaAa')) # Output: 21
print(max_run_uppercase('AaAaAaAaAaAaAaAaAaAaAaAaA')) # Output: 22
print(max_run_uppercase('AaAaAaAaAaAaAaAaAaAaAaAaAa')) # Output: 23
print(max_run_uppercase('AaAaAaAaAaAaAaAaAaAaAaAaAaA')) # Output: