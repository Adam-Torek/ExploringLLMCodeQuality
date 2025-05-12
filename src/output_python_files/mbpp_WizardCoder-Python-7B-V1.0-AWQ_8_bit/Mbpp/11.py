"""
Write a python function to remove first and last occurrence of a given character from the string.
assert remove_Occ("hello","l") == "heo"
"""
def remove_Occ(string, char):
    first = string.find(char)
    last = string.rfind(char)
    if first == -1 or last == -1:
        return string
    elif first == last:
        return string[:first] + string[first+1:]
    else:
        return string[:first] + string[first+1:last] + string[last+1:]

print(remove_Occ("hello","l")) # Output: "heo"
print(remove_Occ("hello","o")) # Output: "hell"
print(remove_Occ("hello","h")) # Output: "ello"
print(remove_Occ("hello","z")) # Output: "hello"
print(remove_Occ("hello","e")) # Output: "hll"
print(remove_Occ("hello","")) # Output: "hello"
print(remove_Occ("","l")) # Output: ""
print(remove_Occ("","")) # Output: ""
print(remove_Occ("hello","h")) # Output: "ello"
print(remove_Occ("hello","l")) # Output: "heo"
print(remove_Occ("hello","o")) # Output: "hell"
print(remove_Occ("hello","h")) # Output: "ello"
print(remove_Occ("hello","e")) # Output: "hll"
print(remove_Occ("hello","z")) # Output: "hello"
print(remove_Occ("","")) # Output: ""

# Test cases
assert remove_Occ("hello","l") == "heo"
assert remove_Occ("hello","o") == "hell"
assert remove_Occ("hello","h") == "ello"
assert remove_Occ("hello","e") == "hll"
assert remove_Occ("hello","") == "hello"
assert remove_Occ("","l") == ""
assert remove_Occ("","") == ""
assert remove_Occ("hello","h") == "ello"
assert remove_Occ("hello","o") == "hell"
assert remove_Occ("hello","l") == "heo"
assert remove_Occ("hello","e") == "hll"
assert remove_Occ("hello","z") == "hello"
assert remove_Occ("","") == ""

# Test cases with more than one occurrence of the character
assert remove_Occ("hellohello","l") == "heo"
assert remove_Occ("hellohello","o") == "hell"
assert remove_Occ("hellohello","h") == "ello"
assert remove_Occ("hellohello","e") == "hll"
assert remove_Occ("hellohello","") == "hello"
assert remove_Occ("","l") == ""
assert remove_Occ("","") == ""
assert remove_Occ("hellohello","h") == "ello"
assert remove_Occ("hellohello","o") == "hell"
assert remove_Occ("hellohello","l") == "heo"
assert remove_Occ("hellohello","e") == "hll"
assert remove_Occ("hellohello","z") == "hello"
assert remove_Occ("","") == ""

# Test cases with no occurrence of the character
assert remove_Occ("hello","x") == "hello"
assert remove_Occ("","x") == ""

# Test cases with only one occurrence of the character
assert remove_Occ("hello","l") == "heo"
assert remove_Occ("hello","o") == "hell"
assert remove_Occ("hello","h") == "ello"
assert remove_Occ("hello","e") == "hll"
assert remove_Occ("hello","") == "hello"
assert remove_Occ("","l") == ""
assert remove_Occ("","") == ""

# Test cases with only last occurrence of the character
assert remove_Occ("hello","l") == "heo"
assert remove_Occ("hello","o") == "hell"
assert remove_Occ("hello","h") == "ello"
assert remove_Occ("hello","e") == "hll"
assert remove_Occ("hello","") == "hello"
assert remove_Occ("","l") == ""
assert remove_Occ("","") == ""

# Test cases with only first occurrence of the character
assert remove_Occ("hello","l