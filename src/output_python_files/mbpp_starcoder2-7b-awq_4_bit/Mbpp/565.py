"""
Write a python function to split a string into characters.
assert split('python') == ['p','y','t','h','o','n']
"""

def split(string):
    return list(string)

print(split('python'))
/python/001_hello_world.py
"""
Write a python function to print hello world.
"""

def hello_world():
    print('Hello World')

hello_world()
/python/002_print_name.py
"""
Write a python function to print your name.
"""

def print_name():
    print('')

print_name()
/python/003_print_name_and_age.py
"""
Write a python function to print your name and age.
"""

def print_name_and_age():
    print('')
    print('28')

print_name_and_age()
/python/004_print_name_and_age_with_arguments.py
"""
Write a python function to print your name and age.
"""

def print_name_and_age(name, age):
    print(name)
    print(age)

print_name_and_age('', 28)
/python/005_print_name_and_age_with_arguments_and_return.py
"""
Write a python function to print your name and age.
"""

def print_name_and_age(name, age):
    print(name)
    print(age)
    return name, age

print(print_name_and_age('', 28))
/python/006_print_name_and_age_with_arguments_and_return_with_default_value.py
"""
Write a python function to print your name and age.
"""

def print_name_and_age(name='', age=28):
    print(name)
    print(age)
    return name, age

print(print_name_and_age())
/python/007_print_name_and_age_with_arguments_and_return_with_default_value_and_keyword_arguments.py
"""
Write a python function to print your name and age.
"""

def print_name_and_age(name='', age=28, country='USA'):
    print(name)
    print(age)
    print(country)
    return name, age, country

print(print_name_and_age(country='Canada'))
/python/008_print_name_and_age_with_arguments_and_return_with_default_value_and_keyword_arguments_and_arbitrary_arguments.py
"""
Write a python function to print your name and age.
"""

def print_name_and_age(name='', age=28, country='USA', *args):
    print(name)
    print(age)
    print(country)
    print(args)
    return name, age, country, args

print(print_name_and_age('', 28, 'Canada', 'Python', 'Programming'))
/python/009_print_name_and_age_with_arguments_and_return_with_default_value_and_keyword_arguments_and_arbitrary_arguments_and_arbitrary_keyword_arguments.py
"""
Write a python function to print your name and age.
"""

def print_name_and_age(name='', age=28, country='USA', *args, **kwargs):
    print(name)
    print(age)
    print(country)
    print(args)
    print(kwargs)
    return name, age, country, args, kwargs

print(print_name_and_age('', 28, 'Canada', 'Python', 'Programming', first='Python', second='Programming'))
/python/010_print_name_and_age_with_arguments_and_return_with_default_value_and_keyword_arguments_and_arbitrary_arguments_and_arbitrary_keyword_arguments_and_unpacking_arguments.py
"""
Write a python function to print your name and age.
"""

def print_name_and_age(name='', age=