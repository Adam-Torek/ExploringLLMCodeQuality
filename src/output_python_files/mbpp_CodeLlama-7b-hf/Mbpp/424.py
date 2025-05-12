"""
Write a function to extract only the rear index element of each string in the given tuple.
assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
"""

def extract_rear(tup):
    return [tup[i][-1] for i in range(len(tup))]

print(extract_rear(('Mers', 'for', 'Vers')))

"""
Write a function to extract only the front index element of each string in the given tuple.
assert extract_front(('Mers', 'for', 'Vers') ) == ['M', 'f', 'V']
"""

def extract_front(tup):
    return [tup[i][0] for i in range(len(tup))]

print(extract_front(('Mers', 'for', 'Vers')))

"""
Write a function to extract only the middle index element of each string in the given tuple.
assert extract_middle(('Mers', 'for', 'Vers') ) == ['e', 'o', 'e']
"""

def extract_middle(tup):
    return [tup[i][1] for i in range(len(tup))]

print(extract_middle(('Mers', 'for', 'Vers')))

"""
Write a function to extract only the last index element of each string in the given tuple.
assert extract_last(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
"""

def extract_last(tup):
    return [tup[i][-1] for i in range(len(tup))]

print(extract_last(('Mers', 'for', 'Vers')))

"""
Write a function to extract only the first index element of each string in the given tuple.
assert extract_first(('Mers', 'for', 'Vers') ) == ['M', 'f', 'V']
"""

def extract_first(tup):
    return [tup[i][0] for i in range(len(tup))]

print(extract_first(('Mers', 'for', 'Vers')))

"""
Write a function to extract only the second index element of each string in the given tuple.
assert extract_second(('Mers', 'for', 'Vers') ) == ['e', 'o', 'e']
"""

def extract_second(tup):
    return [tup[i][1] for i in range(len(tup))]

print(extract_second(('Mers', 'for', 'Vers')))

"""
Write a function to extract only the third index element of each string in the given tuple.
assert extract_third(('Mers', 'for', 'Vers') ) == ['r', 'r', 's']
"""

def extract_third(tup):
    return [tup[i][2] for i in range(len(tup))]

print(extract_third(('Mers', 'for', 'Vers')))

"""
Write a function to extract only the fourth index element of each string in the given tuple.
assert extract_fourth(('Mers', 'for', 'Vers') ) == ['s', 's', 's']
"""

def extract_fourth(tup):
    return [tup[i][3] for i in range(len(tup))]

print(extract_fourth(('Mers', 'for', 'Vers')))

"""
Write a function to extract only the fifth index element of each string in the given tuple.
assert extract_fifth(('Mers', 'for', 'Vers') ) == ['e', 'r', 'e']
"""

def extract_fifth(tup):
    return [tup[i][4] for i in range(len(tup))]

print(extract_fifth(('Mers', 'for', 'Vers')))

"""
Write a function to extract only the sixth index element of each string in the given tuple.
assert extract_sixth(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
"""

def extract_sixth(tup):
    return [