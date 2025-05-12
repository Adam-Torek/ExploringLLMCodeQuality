def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    if file_name.count('.') > 1 or file_name.count('.') == 0:
        return 'No'
    if any(char.isdigit() for char in file_name):
        return 'No'
    if not file_name.split('.')[-1] in ['txt', 'exe', 'dll']:
        return 'No'
    if not file_name.split('.')[0][0].isalpha():
        return 'No'
    return 'Yes'


# Test cases
print(file_name_check("example.txt")) # => 'Yes'
print(file_name_check("1example.dll")) # => 'No'
print(file_name_check("example.exe")) # => 'Yes'
print(file_name_check("example.py")) # => 'No'
print(file_name_check("example.txt.py")) # => 'No'
print(file_name_check("example.dll.exe")) # => 'No'
print(file_name_check("example.txt.exe.dll")) # => 'No'
print(file_name_check("example.exe.txt")) # => 'No'
print(file_name_check("example.dll.txt.exe")) # => 'No'
print(file_name_check("example.exe.dll.txt")) # => 'No'
print(file_name_check("a.exe")) # => 'Yes'
print(file_name_check("A.txt")) # => 'Yes'
print(file_name_check("a.txt.exe.dll")) # => 'No'
print(file_name_check("a.exe.txt.dll")) # => 'No'
print(file_name_check("a.dll.exe.txt")) # => 'No'
print(file_name_check("a.dll.txt.exe")) # => 'No'
print(file_name_check("a.exe.dll")) # => 'Yes'
print(file_name_check("a.txt.dll")) # => 'Yes'
print(file_name_check("a.txt")) # => 'Yes'
print(file_name_check("a.dll")) # => 'Yes'
print(file_name_check("a")) # => 'No'
print(file_name_check("1a.txt")) # => 'No'
print(file_name_check("a1.txt")) # => 'No'
print(file_name_check("a.1txt")) # => 'No'
print(file_name_check("a.exe1")) # => 'No'
print(file_name_check("a.dll1")) # => 'No'
print(file_name_check("1a.dll")) # => 'No'
print(file_name_check("1a.exe")) # => 'No'
print(file_name_check("1a")) # => 'No'
print(file_name_check("a.exe.dll.txt")) # => 'No'
print(file_name_check("a.txt.exe.dll.txt")) # => 'No'
print(file_name_check("a.dll.exe.txt.exe")) # => 'No'
print(file_name_check("a.dll.txt.exe.txt")) # => 'No'
print(