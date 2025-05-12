"""
Write a python function to convert a given string to uppercase.
assert is_upper("person") =="PERSON"
"""
def is_upper(s):
    return s.isupper()

# test
assert is_upper("person") == "PERSON"