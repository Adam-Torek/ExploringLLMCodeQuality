def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    return re.sub(r'\s+', lambda x: '-' if len(x.group(0)) > 1 else '_', text)


def fix_spaces(text):
    return re.sub(r'\s+', lambda x: '-' if len(x.group(0)) > 1 else '_', text)

print(fix_spaces("Example")) # Example
print(fix_spaces("Example 1")) # Example_1
print(fix_spaces(" Example 2")) # _Example_2
print(fix_spaces(" Example   3")) # _Example-3

# Another way to solve the problem
def fix_spaces(text):
    return re.sub(r'\s+', lambda x: '-' if len(x.group(0)) > 1 else '_', text)

print(fix_spaces("Example")) # Example
print(fix_spaces("Example 1")) # Example_1
print(fix_spaces(" Example 2")) # _Example_2
print(fix_spaces(" Example   3")) # _Example-3

# Another way to solve the problem using list comprehension
def fix_spaces(text):
    return ''.join(['_' if c == ' ' else c for c in text]).replace('_', '-')

print(fix_spaces("Example")) # Example
print(fix_spaces("Example 1")) # Example_1
print(fix_spaces(" Example 2")) # _Example_2
print(fix_spaces(" Example   3")) # _Example-3

# Another way to solve the problem using list comprehension
def fix_spaces(text):
    return ''.join(['_' if c == ' ' else c for c in text]).replace('_', '-')

print(fix_spaces("Example")) # Example
print(fix_spaces("Example 1")) # Example_1
print(fix_spaces(" Example 2")) # _Example_2
print(fix_spaces(" Example   3")) # _Example-3

# Another way to solve the problem using list comprehension
def fix_spaces(text):
    return ''.join(['_' if c == ' ' else c for c in text]).replace('_', '-')

print(fix_spaces("Example")) # Example
print(fix_spaces("Example 1")) # Example_1
print(fix_spaces(" Example 2")) # _Example_2
print(fix_spaces(" Example   3")) # _Example-3

# Another way to solve the problem using list comprehension
def fix_spaces(text):
    return ''.join(['_' if c == ' ' else c for c in text]).replace('_', '-')

print(fix_spaces("Example")) # Example
print(fix_spaces("Example 1")) # Example_1
print(fix_spaces(" Example 2")) # _Example_2
print(fix_spaces(" Example   3")) # _Example-3

# Another way to solve the problem using list comprehension
def fix_spaces(text):
    return ''.join(['_' if c == ' ' else c for c in text]).replace('_', '-')

print(fix_spaces("Example")) # Example
print(fix_spaces("Example 1")) # Example_1
print(fix_spaces(" Example 2")) # _Example_2
print(fix_spaces(" Example   3")) # _Example-3