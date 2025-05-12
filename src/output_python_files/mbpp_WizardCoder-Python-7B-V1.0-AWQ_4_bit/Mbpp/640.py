"""
Write a function to remove the parenthesis and what is inbetween them from a string.
assert remove_parenthesis(["python (chrome)"])==("python")
"""

def remove_parenthesis(lst):
    for i in range(len(lst)):
        lst[i] = lst[i].replace("(", "").replace(")", "")
    return lst

print(remove_parenthesis(["python (chrome)"]))