"""
Write a function to check if a string is present as a substring in a given list of string values.
assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
"""

def find_substring(lst, sub):
    for i in lst:
        if sub in i:
            return True
    return False

# assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
# assert find_substring(["red", "black", "white", "green", "orange"],"blue")==False