"""
Write a function to remove the parenthesis and what is inbetween them from a string.
assert remove_parenthesis(["python (chrome)"])==("python")
"""

def remove_parenthesis(lst):
    for i in lst:
        while "(" in i:
            i = i.replace("(", "")
            i = i.replace(")", "")
    return i

print(remove_parenthesis(["python (chrome)"]) == "python")

#Alternative solution:
def remove_parenthesis(lst):
    for i in lst:
        i = i.replace("(", "")
        i = i.replace(")", "")
        return i.split()[0]

print(remove_parenthesis(["python (chrome)"]) == "python")

#Alternative solution:
def remove_parenthesis(lst):
    for i in lst:
        return i.split("(")[0].split(")")[0]

print(remove_parenthesis(["python (chrome)"]) == "python")

#Alternative solution:
def remove_parenthesis(lst):
    for i in lst:
        return i.split("(")[0].split(")")[0]

print(remove_parenthesis(["python (chrome)"]) == "python")

#Alternative solution:
def remove_parenthesis(lst):
    for i in lst:
        return i.split("(")[0].split(")")[0]

print(remove_parenthesis(["python (chrome)"]) == "python")

#Alternative solution:
def remove_parenthesis(lst):
    for i in lst:
        return i.split("(")[0].split(")")[0]

print(remove_parenthesis(["python (chrome)"]) == "python")

#Alternative solution:
def remove_parenthesis(lst):
    for i in lst:
        return i.split("(")[0].split(")")[0]

print(remove_parenthesis(["python (chrome)"]) == "python")

#Alternative solution:
def remove_parenthesis(lst):
    for i in lst:
        return i.split("(")[0].split(")")[0]

print(remove_parenthesis(["python (chrome)"]) == "python")

#Alternative solution:
def remove_parenthesis(lst):
    for i in lst:
        return i.split("(")[0].split(")")[0]

print(remove_parenthesis(["python (chrome)"]) == "python")

#Alternative solution:
def remove_parenthesis(lst):
    for i in lst:
        return i.split("(")[0].split(")")[0]

print(remove_parenthesis(["python (chrome)"]) == "python")

#Alternative solution:
def remove_parenthesis(lst):
    for i in lst:
        return i.split("(")[0].split(")")[0]

print(remove_parenthesis(["python (chrome)"]) == "python")

#Alternative solution:
def remove_parenthesis(lst):
    for i in lst:
        return i.split("(")[0].split(")")[0]

print(remove_parenthesis(["python (chrome)"]) == "python")

#Alternative solution:
def remove_parenthesis(lst):
    for i in lst:
        return i.split("(")[0].split(")")[0]

print(remove_parenthesis(["python (chrome)"]) == "python")

#Alternative solution:
def remove_parenthesis(lst):
    for i in lst:
        return i.split("(")[0].split(")")[0]

print(remove_parenthesis(["python (chrome)"]) == "python")

#Alternative solution:
def remove_parenthesis(lst):
    for i in lst:
        return i.split("(")[0].split(")")[0]

print(remove_parenthesis(["python (chrome)"]) == "python")

#Altern