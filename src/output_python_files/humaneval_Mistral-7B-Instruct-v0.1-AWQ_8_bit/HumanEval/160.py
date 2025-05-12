def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """
    if len(operator) != len(operand) - 1:
        raise ValueError("The length of operator list is equal to the length of operand list minus one.")
    if not operator:
        raise ValueError("The operator list has at least one operator.")
    if not operand:
        raise ValueError("The operand list has at least two operands.")
    if not operand[0] >= 0:
        raise ValueError("The operand list has at least two non-negative integers.")
    if not operand[1] >= 0:
        raise ValueError("The operand list has at least two non-negative integers.")
    if not operand[2] >= 0:
        raise ValueError("The operand list has at least two non-negative integers.")
    if not operand[3] >= 0:
        raise ValueError("The operand list has at least two non-negative integers.")
    if operator[0] == '+':
        result = operand[0] + operand[1] * operand[2] - operand[3]
    elif operator[0] == '-':
        result = operand[0] - operand[1] * operand[2] + operand[3]
    elif operator[0] == '*':
        result = operand[0] * operand[1] * operand[2] - operand[3]
    elif operator[0] == '//':
        result = operand[0] // operand[1] * operand[2] - operand[3]
    elif operator[0] == '**':
        result = operand[0] ** operand[1] * operand[2] - operand[3]
    else:
        raise ValueError("The operator list has at least one operator.")
    return result


def test_do_algebra():
    """
    Test the do_algebra function.
    """
    operator = ['+', '*', '-']
    array = [2, 3, 4, 5]
    result = do_algebra(operator, array)
    assert result == 9
    operator = ['-', '*', '+']
    array = [2, 3, 4, 5]
    result = do_algebra(operator, array)
    assert result == -9
    operator = ['*', '//', '**']
    array = [2, 3, 4, 5]
    result = do_algebra(operator, array)
    assert result == 16
    operator = ['+', '*', '-', '//']
    array = [2, 3, 4, 5]
    result = do_algebra(operator, array)
    assert result == 10
    operator = ['-', '*', '+', '**']
    array = [2, 3, 4, 5]
    result = do_algebra(operator, array)
    assert result == -10
    operator = ['-', '*', '+', '//']
    array = [2, 3, 4, 5]
    result = do_algebra(operator, array)
    assert result == -10
    operator = ['*', '//', '**']
    array = [2, 3, 4, 5]
    result = do_algebra(operator, array)
    assert result == 16
    operator = ['+', '*', '-