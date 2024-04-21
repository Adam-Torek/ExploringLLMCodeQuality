"""
Write a function to remove odd characters in a string.
assert remove_odd("python")==("yhn")
"""
def remove_odd(string):
    return ''.join(char for char in string if char % 2 == 0)

# Test the function
assert remove_odd("python") == "yhn"<|endoftext|>