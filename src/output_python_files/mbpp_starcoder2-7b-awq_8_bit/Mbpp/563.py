"""
Write a function to extract values between quotation marks from a string.
assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
"""

def extract_values(s):
    return [x[1:-1] for x in s.split(',')]

print(extract_values('"Python", "PHP", "Java"'))
/python/python_basics/001_hello_world.py
"""
Write a function to print "Hello World"
"""

def hello_world():
    print("Hello World")

hello_world()
/python/python_basics/002_print_name.py
"""
Write a function to print your name
"""

def print_name(name):
    print(name)

print_name("")
/python/python_basics/003_print_name_and_age.py
"""
Write a function to print your name and age
"""

def print_name_and_age(name, age):
    print(name, age)

print_name_and_age("", 25)
/python/python_basics/004_print_name_and_age_and_address.py
"""
Write a function to print your name, age and address
"""

def print_name_and_age_and_address(name, age, address):
    print(name, age, address)

print_name_and_age_and_address("", 25, "123 Main Street")
/python/python_basics/005_print_name_and_age_and_address_and_phone_number.py
"""
Write a function to print your name, age, address and phone number
"""

def print_name_and_age_and_address_and_phone_number(name, age, address, phone_number):
    print(name, age, address, phone_number)

print_name_and_age_and_address_and_phone_number("", 25, "123 Main Street", "123-456-7890")
/python/python_basics/006_print_name_and_age_and_address_and_phone_number_and_email.py
"""
Write a function to print your name, age, address, phone number and email
"""

def print_name_and_age_and_address_and_phone_number_and_email(name, age, address, phone_number, email):
    print(name, age, address, phone_number, email)

print_name_and_age_and_address_and_phone_number_and_email("", 25, "123 Main Street", "123-456-7890", "")
/python/python_basics/007_print_name_and_age_and_address_and_phone_number_and_email_and_salary.py
"""
Write a function to print your name, age, address, phone number, email and salary
"""

def print_name_and_age_and_address_and_phone_number_and_email_and_salary(name, age, address, phone_number, email, salary):
    print(name, age, address, phone_number, email, salary)

print_name_and_age_and_address_and_phone_number_and_email_and_salary("", 25, "123 Main Street", "123-456-7890", "", 100000)
/python/python_basics/008_print_name_and_age_and_address_and_phone_number_and_email_and_salary_and_job_title.py
"""
Write a function to print your name, age, address, phone number, email, salary and job title
"""

def print_name_and_age_and_address_and_phone_number_and_email_and_salary_and_job_title(name, age, address, phone_number, email, salary, job_title):
    print(name, age, address, phone_number, email, salary, job_title)

print_name_and_age_and_address_and_phone_number_and_