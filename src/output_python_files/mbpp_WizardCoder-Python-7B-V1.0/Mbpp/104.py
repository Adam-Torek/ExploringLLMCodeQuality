"""
Write a function to sort each sublist of strings in a given list of lists.
assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
"""

def sort_sublists(lst):
    for i in range(len(lst)):
        lst[i].sort()
    return lst

print(sort_sublists([["green", "orange"], ["black", "white"], ["white", "black", "orange"]]))

# Output: [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]