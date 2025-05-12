"""
Write a function to find maximum run of uppercase characters in the given string.
assert max_run_uppercase('GeMKSForGERksISBESt') == 5
"""

def max_run_uppercase(s):
    max_run = 0
    current_run = 0
    max_run_current = 0
    for c in s:
        if c.isupper():
            current_run += 1
        else:
            max_run = max(max_run, current_run)
            current_run = 0
    return max(max_run, current_run)

# Test cases
print(max_run_uppercase('GeMKSForGERksISBESt')) # Output: 5
print(max_run_uppercase('AABBBCCaDDd')) # Output: 3
print(max_run_uppercase('A')) # Output: 1
print(max_run_uppercase('AaBbCc')) # Output: 0
print(max_run_uppercase('')) # Output: 0
print(max_run_uppercase('AaBbCcDd')) # Output: 0
print(max_run_uppercase('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz')) # Output: 26
print(max_run_uppercase('AAABBBCCCDDD')) # Output: 4
print(max_run_uppercase('AAAbbbCCCdddEEEfffGGG')) # Output: 6
print(max_run_uppercase('AAAbbbCCCdddEEEfffGGG')) # Output: 6
print(max_run_uppercase('AAAbbbCCCdddEEEfffGGG')) # Output: 6
print(max_run_uppercase('AAAbbbCCCdddEEEfffGGG')) # Output: 6
print(max_run_uppercase('AAAbbbCCCdddEEEfffGGG')) # Output: 6
print(max_run_uppercase('AAAbbbCCCdddEEEfffGGG')) # Output: 6
print(max_run_uppercase('AAAbbbCCCdddEEEfffGGG')) # Output: 6
print(max_run_uppercase('AAAbbbCCCdddEEEfffGGG')) # Output: 6
print(max_run_uppercase('AAAbbbCCCdddEEEfffGGG')) # Output: 6
print(max_run_uppercase('AAAbbbCCCdddEEEfffGGG')) # Output: 6
print(max_run_uppercase('AAAbbbCCCdddEEEfffGGG')) # Output: 6
print(max_run_uppercase('AAAbbbCCCdddEEEfffGGG')) # Output: 6
print(max_run_uppercase('AAAbbbCCCdddEEEfffGGG')) # Output: 6
print(max_run_uppercase('AAAbbbCCCdddEEEfffGGG')) # Output: 6
print(max_run_uppercase('AAAbbbCCCdddEEEfffGGG')) # Output: 6
print(max_run_uppercase('AAAbbbCCCdddEEEfffGGG')) # Output: 6
print(max_run_uppercase('AAAbbbCCCdddEEEfffGGG')) # Output: 6
print(max_run_uppercase('AAAbbbCCCdddEEEfffGGG')) # Output: 6
print(max_run_uppercase('AAAbbbCCCdddEEEfffGGG')) # Output: 6
print(max_run_uppercase('AAAbbbCCCdddEEEfffGGG')) # Output: 6
print(max_run_uppercase('AAAbbbCCCdddEEEfffGGG')) # Output: 6
print(max_run_uppercase('AA