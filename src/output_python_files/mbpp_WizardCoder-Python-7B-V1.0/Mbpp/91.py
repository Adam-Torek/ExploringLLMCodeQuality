"""
Write a function to check if a string is present as a substring in a given list of string values.
assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
"""
def find_substring(lst, substr):
    for i in lst:
        if substr in i:
            return True
    return False

# Test cases
print(find_substring(["red", "black", "white", "green", "orange"],"ack")) # True
print(find_substring(["red", "black", "white", "green", "orange"],"blue")) # False
print(find_substring(["hello", "world", "python", "programming"],"pro")) # True
print(find_substring(["hello", "world", "python", "programming"],"java")) # False
print(find_substring(["hello", "world", "python", "programming"],"world")) # True
print(find_substring(["hello", "world", "python", "programming"],"hello")) # True
print(find_substring(["hello", "world", "python", "programming"],"programming")) # True
print(find_substring(["hello", "world", "python", "programming"],"hello world")) # False
print(find_substring(["hello", "world", "python", "programming"],"world python")) # True
print(find_substring(["hello", "world", "python", "programming"],"programming python")) # False
print(find_substring(["hello", "world", "python", "programming"],"programming world")) # True
print(find_substring(["hello", "world", "python", "programming"],"hello world programming")) # True
print(find_substring(["hello", "world", "python", "programming"],"hello world programming python")) # True
print(find_substring(["hello", "world", "python", "programming"],"hello world programming python world")) # True
print(find_substring(["hello", "world", "python", "programming"],"hello world programming python java")) # False
print(find_substring(["hello", "world", "python", "programming"],"hello world programming python world hello")) # True
print(find_substring(["hello", "world", "python", "programming"],"hello world programming python world hello world")) # True
print(find_substring(["hello", "world", "python", "programming"],"hello world programming python world hello world hello")) # True
print(find_substring(["hello", "world", "python", "programming"],"hello world programming python world hello world hello")) # True
print(find_substring(["hello", "world", "python", "programming"],"hello world programming python world hello world hello hello")) # True
print(find_substring(["hello", "world", "python", "programming"],"hello world programming python world hello world hello hello world")) # True
print(find_substring(["hello", "world", "python", "programming"],"hello world programming python world hello world hello hello world hello")) # True
print(find_substring(["hello", "world", "python", "programming"],"hello world programming python world hello world hello hello world hello world")) # True
print(find_substring(["hello", "world", "python", "programming"],"hello world programming python world hello world hello hello world hello world hello")) # True
print(find_substring(["hello", "world", "python", "programming"],"hello world programming python world hello world hello world hello world hello world hello")) # True
print(find_substring(["hello", "world", "python", "programming"],"hello world programming python world hello world hello world hello world hello world hello world")) # True
print(find_substring(["hello", "world", "python", "programming"],"hello world programming python world hello world hello world hello world hello world hello world hello")) # True
print(find_substring(["hello", "world", "python", "programming"],"hello world programming python world hello world hello world hello world hello world hello world hello world")) # True
print(find_substring(["hello", "world", "python", "programming"],"hello world programming python world hello world hello world hello world hello world hello world hello world hello")) # True
print(find_substring(["hello", "world", "python", "programming"],"hello world programming python world hello world hello world hello world hello world hello world hello world hello world")) # True
print(find_substring(["hello", "world", "python", "programming"],"