"""
Write a function to check if a string is present as a substring in a given list of string values.
assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
"""
def find_substring(arr, substr):
    for string in arr:
        if substr in string:
            return True
    return False

# Test case
assert find_substring(["red", "black", "white", "green", "orange"], "ack") == True
assert find_substring(["red", "black", "white", "green", "orange"], "apple") == False