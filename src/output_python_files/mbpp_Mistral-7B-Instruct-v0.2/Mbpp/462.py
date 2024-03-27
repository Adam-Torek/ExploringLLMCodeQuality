"""
Write a function to find all possible combinations of the elements of a given list.
assert combinations_list(['orange', 'red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]
"""
def combinations_list(input_list):
    """
    This function generates all possible combinations of the elements of a given list.

    Parameters:
    input_list (list): The list from which we want to generate all possible combinations.

    Returns:
    list: A list containing all possible combinations of the elements of the input list.
    """
    if len(input_list) == 0:
        return [[]]

    result = []
    for i in range(len(input_list)):
        sub_list = input_list[:i] + input_list[i+1:]
        for combination in combinations_list(sub_list):
            result.append([input_list[i]] + combination)

    return result

assert combinations_list(['orange', 'red', 'green', 'blue']) == [[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]</s>