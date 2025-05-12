"""
Write a function to find all possible combinations of the elements of a given list.
assert combinations_list(['orange', 'red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]
"""
def combinations_list(input_list):
    """
    This function returns all possible combinations of the elements of a given list.

    Args:
        input_list: list of elements

    Returns:
        list: list of all possible combinations of the elements of the input list
    """
    if len(input_list) == 0:
        return [[]]

    combinations = []
    for i in range(len(input_list)):
        sub_combinations = combinations_list(input_list[i+1:])
        for sub_combination in sub_combinations:
            combinations.append([input_list[i]] + sub_combination)

    return combinations

assert combinations_list(['orange', 'red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]