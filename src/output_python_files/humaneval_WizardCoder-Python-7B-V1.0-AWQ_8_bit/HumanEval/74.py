def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''
    total_chars = 0
    for i in lst1:
        total_chars += len(i)
    for j in lst2:
        total_chars += len(j)
    if total_chars < len(lst1):
        return lst1
    else:
        return lst2

# Test cases
print(total_match([], [])) # []
print(total_match(['hi', 'admin'], ['hI', 'Hi'])) # ['hI', 'Hi']
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])) # ['hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi'])) # ['hI', 'hi', 'hi']
print(total_match(['4'], ['1', '2', '3', '4', '5'])) # ['4']
print(total_match(['hi', 'admin'], ['hi', 'admin'])) # ['hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'Hi', 'project'])) # ['hI', 'Hi']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'admin'])) # ['hI', 'hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi'])) # ['hI', 'hi']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'admin', 'project', '123'])) # ['hI', 'hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'admin', 'project', '123', '456'])) # ['hI', 'hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'admin', 'project', '123', '456', '789'])) # ['hI', 'hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'admin', 'project', '123', '456', '789', '10111'])) # ['hI', 'hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'admin', 'project', '123', '456', '789', '1011', '1213'])) # ['hI', 'hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'admin', 'project', '123', '456', '789', '1011', '1213', '1415'])) # ['hI', 'hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'admin', 'project', '123', '456', '789', '1011', '1213', '1415', '1617'])) # ['hI', 'hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'admin', 'project', '123', '456', '789', '1011', '1213', '1415', '1617', '1819'])) # ['hI