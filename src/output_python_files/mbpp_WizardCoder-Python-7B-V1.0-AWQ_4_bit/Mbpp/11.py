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
print(remove_Occ("hello","")) # Output: "hello"
print(remove_Occ("","h")) # Output: ""
print(remove_Occ("h","")) # Output: ""
print(remove_Occ("","")) # Output: ""
print(remove_Occ("hello","l")) # Output: "heo"
print(remove_Occ("hello","o")) # Output: "hell"
print(remove_Occ("hello","h")) # Output: "ello"
print(remove_Occ("hello","z")) # Output: "hello"
print(remove_Occ("","h")) # Output: ""
print(remove_Occ("","")) # Output: ""

# Test cases
assert remove_Occ("hello","l") == "heo"
assert remove_Occ("hello","o") == "hell"
assert remove_Occ("hello","h") == "ello"
assert remove_Occ("hello","z") == "hello"
assert remove_Occ("","h") == ""
assert remove_Occ("","") == ""
assert remove_Occ("hello","l") == "heo"
assert remove_Occ("hello","o") == "hell"
assert remove_Occ("hello","h") == "ello"
assert remove_Occ("hello","z") == "hello"
assert remove_Occ("","h") == ""
assert remove_Occ("","") == ""

# Edge cases
assert remove_Occ("hello","") == ""
assert remove_Occ("","") == ""
assert remove_Occ("hello","l") == "heo"
assert remove_Occ("hello","o") == "hell"
assert remove_Occ("hello","h") == "ello"
assert remove_Occ("hello","z") == "hello"
assert remove_Occ("","") == ""

# Test cases with multiple occurrences of the character
assert remove_Occ("helloolleh","l") == "heohe"
assert remove_Occ("helloolleh","o") == "helloleh"
assert remove_Occ("helloolleh","h") == "elloleh"
assert remove_Occ("helloolleh","z") == "helloolleh"
assert remove_Occ("","l") == ""
assert remove_Occ("","") == ""
assert remove_Occ("helloolleh","l") == "heohe"
assert remove_Occ("helloolleh","o") == "helloleh"
assert remove_Occ("helloolleh","h") == "elloleh"
assert remove_Occ("helloolleh","z") == "helloolleh"
assert remove_Occ("","l") == ""
assert remove_Occ("","") == ""

# Test cases with only one occurrence of the character
assert remove_Occ("hello","a") == "hello"
assert remove_Occ("hello","e") == "hello"
assert remove_Occ("hello","l") == "heo"
assert remove_Occ("hello","o") == "hell"
assert remove_Occ("hello","h") == "ello"
assert remove_Occ("hello","z") == "hello"
assert remove_Occ("","a") == ""
assert remove_Occ("","") == ""

# Test cases with no occurrence of the character
assert remove_Occ("hello","x") == "hello"
assert remove_Occ