"""
Write a function to check if a string is present as a substring in a given list of string values.
assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
"""

def find_substring(lst, sub):
    for i in lst:
        if sub in i:
            return True
    return False

# Test cases
print(find_substring(["red", "black", "white", "green", "orange"],"ack")==True) # True
print(find_substring(["red", "black", "white", "green", "orange"],"blue")==False) # False
print(find_substring(["red", "black", "white", "green", "orange"],"")==False) # False
print(find_substring(["red", "black", "white", "green", "orange"],"red")==True) # True
print(find_substring(["red", "black", "white", "green", "orange"],"r")==True) # True
print(find_substring(["red", "black", "white", "green", "orange"],"e")==True) # True
print(find_substring(["red", "black", "white", "green", "orange"],"e")==True) # True
print(find_substring(["red", "black", "white", "green", "orange"],"")==False) # False
print(find_substring(["red", "black", "white", "green", "orange"],"r")==True) # True
print(find_substring(["red", "black", "white", "green", "orange"],"e")==True) # True
print(find_substring(["red", "black", "white", "green", "orange"],"")==False) # False

# Edge cases
print(find_substring([],"")==False) # False
print(find_substring([],"a")==False) # False
print(find_substring([""],"")==False) # False
print(find_substring([""],"a")==False) # False
print(find_substring(["a"],"")==False) # False
print(find_substring(["a"],"a")==True) # True
print(find_substring(["a"],"b")==False) # False
print(find_substring(["a"],"aa")==False) # False
print(find_substring(["a"],"ab")==False) # False
print(find_substring(["a"],"ba")==False) # False
print(find_substring(["a"],"aba")==False) # False
print(find_substring(["a"],"abba")==False) # False
print(find_substring(["a"],"abc")==False) # False
print(find_substring(["a"],"abc")==False) # False
print(find_substring(["a"],"abc")==False) # False
print(find_substring(["a"],"abc")==False) # False
print(find_substring(["a"],"abc")==False) # False
print(find_substring(["a"],"abc")==False) # False
print(find_substring(["a"],"abc")==False) # False
print(find_substring(["a"],"abc")==False) # False
print(find_substring(["a"],"abc")==False) # False
print(find_substring(["a"],"abc")==False) # False
print(find_substring(["a"],"abc")==False) # False
print(find_substring(["a"],"abc")==False) # False
print(find_substring(["a"],"abc")==False) # False
print(find_substring(["a"],"abc")==False) # False
print(find_substring(["a"],"abc")==False) # False
print(find_substring(["a"],"abc")==False) # False
print(find_substring(["a"],"abc")==False) # False
print(find_substring(["a"],"abc")==False) # False
print(find_substring(["a"],"abc")==False) # False
print(find_substring(["a"],"abc")==False) # False
print(find_substring(["a"],"abc")==False) # False
print(