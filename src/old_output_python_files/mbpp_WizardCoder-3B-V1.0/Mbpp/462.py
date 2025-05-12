"""
Write a function to find all possible combinations of the elements of a given list.
assert combinations_list(['orange','red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green','red'], ['green','red', 'orange'], ['blue'], ['blue', 'orange'], ['blue','red'], ['blue','red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green','red'], ['blue', 'green','red', 'orange']]
"""

def combinations_list(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            result.append(lst[i:j])
    return result

print(combinations_list(['orange','red', 'green', 'blue']))<|endoftext|>