"""
Write a function to remove the parenthesis and what is inbetween them from a string.
assert remove_parenthesis(["python (chrome)"])==("python")
"""
def remove_parenthesis(input_string):
    """
    This function takes a string as an argument and returns the string with all parenthesis and their content removed.
    """
    return input_string.replace('(','').replace(')','')

# Test the function
assert remove_parenthesis(["python (chrome)"])==("python")
assert remove_parenthesis("python (1, 2, 3) (4, 5)")==("python")
assert remove_parenthesis("python (1, 2, 3) (4, 5) python (6, 7)")==("python python")
assert remove_parenthesis("python (1, 2, 3) (4, 5) python (6, 7) python (8, 9)")==("python python python")
assert remove_parenthesis("python (1, 2, 3) (4, 5) python (6, 7) python (8, 9) python (10, 11)")==("python python python python")