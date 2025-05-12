"""
Write a function to find maximum run of uppercase characters in the given string.
assert max_run_uppercase('GeMKSForGERksISBESt') == 5
"""

def max_run_uppercase(s):
    max_run = 0
    current_run = 0
    for i in range(len(s)):
        if s[i].isupper():
            current_run += 1
        else:
            if current_run > max_run:
                max_run = current_run
            current_run = 0
    if current_run > max_run:
        max_run = current_run
    return max_run

# Test cases
print(max_run_uppercase('GeMKSForGERksISBESt')) # Output: 5<|endoftext|>