"""
Write a python function to check whether all the characters are same or not.
assert all_Characters_Same("python") == False
"""
def all_Characters_Same(string):
    if len(string) == 1:
        return True
    else:
        return string[0] == string[-1] and all_Characters_Same(string[1:-1])

# Test cases
print(all_Characters_Same("python")) # False
print(all_Characters_Same("hello")) # True
print(all_Characters_Same("abc")) # True<|endoftext|>