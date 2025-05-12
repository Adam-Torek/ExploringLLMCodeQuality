"""
Write a function to find the occurrence and position of the substrings within a string. Return None if there is no match.
assert occurance_substring('python programming, python language','python')==('python', 0, 6)
"""

def occurance_substring(string, substring):
    """
    :param string: string
    :param substring: substring
    :return: None if there is no match, otherwise return a tuple of (substring, start_index, end_index)
    """
    # TODO: Write your code here
    pass

if __name__ == '__main__':
    print(occurance_substring('python programming, python language', 'python'))
/python/01_basic/02_list/01_list_basic.py
"""
List is a collection which is ordered and changeable. Allows duplicate members.
"""

# Create a list
list_1 = ['apple', 'banana', 'cherry']
list_2 = list(('apple', 'banana', 'cherry'))
list_3 = list(range(10))

# Access items
print(list_1[0])
print(list_1[-1])

# Change items
list_1[0] = 'orange'
print(list_1)

# Loop through a list
for item in list_1:
    print(item)

# Check if item exists
if 'apple' in list_1:
    print('apple exists')

# Get the length of a list
print(len(list_1))

# Add items
list_1.append('grape')
print(list_1)

# Insert items
list_1.insert(1,'mango')
print(list_1)

# Remove items
list_1.remove('mango')
print(list_1)

# Remove the last item
list_1.pop()
print(list_1)

# Remove the item at a specific position
list_1.pop(1)
print(list_1)

# Remove the specified item
list_1.remove('banana')
print(list_1)

# Clear the list
list_1.clear()
print(list_1)

# Delete the list
del list_1

# Join two lists
list_1 = ['apple', 'banana', 'cherry']
list_2 = ['grape','mango']
list_1.extend(list_2)
print(list_1)

# Copy a list
list_1 = ['apple', 'banana', 'cherry']
list_2 = list_1.copy()
print(list_2)

# Sort a list
list_1 = ['apple', 'banana', 'cherry']
list_1.sort()
print(list_1)

# Reverse a list
list_1 = ['apple', 'banana', 'cherry']
list_1.reverse()
print(list_1)

# Copy a list
list_1 = ['apple', 'banana', 'cherry']
list_2 = list_1
print(list_2)

# Copy a list
list_1 = ['apple', 'banana', 'cherry']
list_2 = list_1[:]
print(list_2)

# Copy a list
list_1 = ['apple', 'banana', 'cherry']
list_2 = list_1.copy()
print(list_2)

# Copy a list
list_1 = ['apple', 'banana', 'cherry']
list_2 = list_1.copy()
print(list_2)

# Copy a list
list_1 = ['apple', 'banana', 'cherry']
list_2 = list_1.copy()
print(list_2)

# Copy a list
list_1 = ['apple', 'banana', 'cherry']
list_2 = list_1.copy()
print(list_2)

# Copy a list
list_1 = ['apple', 'banana', 'cherry']
list_2 = list_1.copy()