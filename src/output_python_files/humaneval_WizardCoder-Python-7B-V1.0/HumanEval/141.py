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
    if file_name.count('.') != 1:
        return 'No'
    if file_name.count('0') > 3 or file_name.count('1') > 3 or file_name.count('2') > 3 or file_name.count('3') > 3 or file_name.count('4') > 3 or file_name.count('5') > 3 or file_name.count('6') > 3 or file_name.count('7') > 3 or file_name.count('8') > 3 or file_name.count('9') > 3:
        return 'No'
    if file_name.split('.')[-1] not in ['txt', 'exe', 'dll']:
        return 'No'
    if not file_name.split('.')[0][0].isalpha():
        return 'No'
    return 'Yes'

# Test cases
print(file_name_check("example.txt")) # => 'Yes'
print(file_name_check("1example.dll")) # => 'No'
print(file_name_check("example.exe")) # => 'Yes'
print(file_name_check("example.py")) # => 'No'
print(file_name_check("example.txt.exe")) # => 'No'
print(file_name_check("example.dll.exe")) # => 'No'
print(file_name_check("example.exe.txt")) # => 'No'
print(file_name_check("example.exe.dll.txt")) # => 'No'
print(file_name_check("example.exe.dll.exe")) # => 'No'
print(file_name_check("example.exe.dll.exe.txt")) # => 'No'
print(file_name_check("example.exe.dll.exe.exe")) # => 'No'
print(file_name_check("example.exe.dll.exe.dll")) # => 'No'
print(file_name_check("example.exe.dll.exe.txt.exe")) # => 'No'
print(file_name_check("example.exe.dll.exe.dll.txt")) # => 'No'
print(file_name_check("example.exe.dll.exe.dll.exe.txt")) # => 'No'
print(file_name_check("example.exe.dll.exe.dll.exe.exe")) # => 'No'
print(file_name_check("example.exe.dll.exe.dll.exe.dll")) # => 'No'
print(file_name_check("example.exe.dll.exe.dll.exe.txt.exe")) # => 'No'
print(file_name_check("example.exe.dll.exe.dll.exe.dll.txt")) # => 'No'
print(file_name_check("example.exe.dll.exe.dll.exe.dll.exe.txt")) # => 'No'
print(file_name_check("example.exe.dll.exe.dll.exe.dll.exe.exe")) # => 'No'
print(file_name_check("a.txt")) # => 'Yes'
print(file_name_check("A.txt")) # => 'Yes'
print(file_name_check("a.exe")) # => 'Yes'
print(file_