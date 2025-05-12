"""
Write a function to toggle the case of all characters in a string.
assert toggle_string("Python")==("pYTHON")
"""
def toggle_string(string):
    return string.swapcase()

print(toggle_string("Python"))

"""
Write a function to count the number of words in a string.
assert count_words("Python is a programming language")==4
"""
def count_words(string):
    return len(string.split())

print(count_words("Python is a programming language"))

"""
Write a function to count the number of occurrences of a substring in a string.
assert count_substring("Python is a programming language","is")==2
"""
def count_substring(string,substring):
    return string.count(substring)

print(count_substring("Python is a programming language","is"))

"""
Write a function to convert a string to a list.
assert convert_string_to_list("Python is a programming language")==['P','y','t','h','o','n',' ','i','s',' ','a',' ','p','r','o','g','r','a','m','m','i','n','g',' ','l','a','n','g','u','a','g','e']
"""
def convert_string_to_list(string):
    return list(string)

print(convert_string_to_list("Python is a programming language"))

"""
Write a function to convert a list to a string.
assert convert_list_to_string(['P','y','t','h','o','n',' ','i','s',' ','a',' ','p','r','o','g','r','a','m','m','i','n','g',' ','l','a','n','g','u','a','g','e'])=="Python is a programming language"
"""
def convert_list_to_string(list):
    return ''.join(list)

print(convert_list_to_string(['P','y','t','h','o','n',' ','i','s',' ','a',' ','p','r','o','g','r','a','m','m','i','n','g',' ','l','a','n','g','u','a','g','e']))

"""
Write a function to convert a list of characters into a string.
assert convert_list_of_characters_to_string(['P','y','t','h','o','n',' ','i','s',' ','a',' ','p','r','o','g','r','a','m','m','i','n','g',' ','l','a','n','g','u','a','g','e'])=="Python is a programming language"
"""
def convert_list_of_characters_to_string(list):
    return ''.join(list)

print(convert_list_of_characters_to_string(['P','y','t','h','o','n',' ','i','s',' ','a',' ','p','r','o','g','r','a','m','m','i','n','g',' ','l','a','n','g','u','a','g','e']))

"""
Write a function to convert a list of characters into a string.
assert convert_list_of_characters_to_string(['P','y','t','h','o','n',' ','i','s',' ','a',' ','p','r','o','g','r','a','m','m','i','n','g',' ','l','a','n','g','u','a','g','e'])=="Python is a programming language"
"""
def convert_list_of_characters_to_string(list):
    return ''.join(list)

print(convert_list_of_characters_to_string(['P','y','t','h','o','n',' ','i','s',' ','a',' ','p','r','o','g','r','a','m','m','i','n','g',' ','l','a','n','g','u','a','g','e']))

"""
Write a function to convert a list of characters into a string.
assert convert_list_of_characters_to_string(['P','y','t','h','o','n',' ','i','s',' ','a',' ','p','r','o','g','r','a','m','m','i','n','g',' ','l','a','n','g','u','a','g','e'])=="