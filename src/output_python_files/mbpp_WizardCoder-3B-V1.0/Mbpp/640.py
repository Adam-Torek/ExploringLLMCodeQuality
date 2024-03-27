"""
Write a function to remove the parenthesis and what is inbetween them from a string.
assert remove_parenthesis(["python (chrome)"])==("python")
"""

def remove_parenthesis(s):
    return s.strip("()")

# Test the function
print(remove_parenthesis(["python (chrome)"])==("python"))<|endoftext|>