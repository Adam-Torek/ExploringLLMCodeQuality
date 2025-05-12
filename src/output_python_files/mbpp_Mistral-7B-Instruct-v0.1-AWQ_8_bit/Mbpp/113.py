"""
Write a function to check if a string represents an integer or not.
assert check_integer("python")==False
"""

def check_integer(s):
    try:
        int(s)
        return True
    except:
        return False

assert check_integer("python")==False
assert check_integer("123")==True
assert check_integer("123a")==False