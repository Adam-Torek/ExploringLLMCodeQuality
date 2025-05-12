"""
Write a function to check if a string is present as a substring in a given list of string values.
assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
"""


def find_substring(list_of_strings, substring):
    for string in list_of_strings:
        if substring in string:
            return True
    return False


print(find_substring(["red", "black", "white", "green", "orange"], "ack"))
print(find_substring(["red", "black", "white", "green", "orange"], "acka"))
print(find_substring(["red", "black", "white", "green", "orange"], "ackb"))
print(find_substring(["red", "black", "white", "green", "orange"], "ackc"))
print(find_substring(["red", "black", "white", "green", "orange"], "ackd"))
print(find_substring(["red", "black", "white", "green", "orange"], "acke"))
print(find_substring(["red", "black", "white", "green", "orange"], "ackf"))
print(find_substring(["red", "black", "white", "green", "orange"], "ackg"))
print(find_substring(["red", "black", "white", "green", "orange"], "ackh"))
print(find_substring(["red", "black", "white", "green", "orange"], "acki"))
print(find_substring(["red", "black", "white", "green", "orange"], "ackj"))
print(find_substring(["red", "black", "white", "green", "orange"], "ackk"))
print(find_substring(["red", "black", "white", "green", "orange"], "ackl"))
print(find_substring(["red", "black", "white", "green", "orange"], "ackm"))
print(find_substring(["red", "black", "white", "green", "orange"], "ackn"))
print(find_substring(["red", "black", "white", "green", "orange"], "acko"))
print(find_substring(["red", "black", "white", "green", "orange"], "ackp"))
print(find_substring(["red", "black", "white", "green", "orange"], "ackq"))
print(find_substring(["red", "black", "white", "green", "orange"], "ackr"))
print(find_substring(["red", "black", "white", "green", "orange"], "acks"))
print(find_substring(["red", "black", "white", "green", "orange"], "ackt"))
print(find_substring(["red", "black", "white", "green", "orange"], "acku"))
print(find_substring(["red", "black", "white", "green", "orange"], "ackv"))
print(find_substring(["red", "black", "white", "green", "orange"], "ackw"))
print(find_substring(["red", "black", "white", "green", "orange"], "ackx"))
print(find_substring(["red", "black", "white", "green", "orange"], "acky"))
print(find_substring(["red", "black", "white", "green", "orange"], "ackz"))
print(find_substring(["red", "black", "white", "green", "orange"], "ack0"))
print(find_substring(["red", "black", "white", "green", "orange"], "ack1"))
print(find_substring(["red", "black", "white", "green", "orange"], "ack2"))
print(find_substring(["red", "black", "white", "green", "orange"], "ack3"))
print(find_substring(["red", "black", "white", "green", "orange"], "ack4"))
print(find_substring(["red", "black", "white", "green", "orange"], "ack5"))
print(find_substring(["red", "black", "white", "green", "orange"], "ack6"))
print(find_substring(["red",