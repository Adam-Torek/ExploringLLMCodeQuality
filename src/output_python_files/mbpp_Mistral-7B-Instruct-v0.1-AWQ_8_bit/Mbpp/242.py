"""
Write a function to count the total number of characters in a string.
assert count_charac("python programming")==18
"""
def count_charac(string):
    total=0
    for i in string:
        total+=1
    return total

#assert count_charac("python programming")==18
print(count_charac("python programming"))