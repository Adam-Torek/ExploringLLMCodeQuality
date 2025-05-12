"""
Write a function to find all possible combinations of the elements of a given list.
assert combinations_list(['orange', 'red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]
"""

def combinations_list(lst):
    def helper(lst, current_combination, result):
        if not lst:
            result.append(current_combination)
        else:
            helper(lst[1:], current_combination + [lst[0]], result)
            helper(lst[1:], current_combination, result)
            helper(lst[1:], current_combination, result)
    result = []
    helper(lst, [], result)
    return result

print(combinations_list(['orange', 'red', 'green', 'blue']))