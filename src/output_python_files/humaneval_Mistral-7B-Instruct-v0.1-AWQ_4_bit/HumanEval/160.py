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
    if not operator or not operand:
        raise ValueError("Operator and operand list must have at least one operator and one operand.")
    operator_dict = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '//': lambda x, y: x // y, '**': lambda x, y: x ** y}
    result = operand[0]
    for i in range(1, len(operand)):
        result = operator_dict[operator[i-1]](result, operand[i])
    return result


def test_do_algebra():
    """
    Test the do_algebra function.
    """
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    result = do_algebra(operator, operand)
    assert result == 9

    operator = ['-', '*', '+']
    operand = [5, 2, 3, 4]
    result = do_algebra(operator, operand)
    assert result == 11

    operator = ['*', '//', '+']
    operand = [10, 2, 3, 4]
    result = do_algebra(operator, operand)
    assert result == 14

    operator = ['**', '//', '+']
    operand = [10, 2, 3, 4]
    result = do_algebra(operator, operand)
    assert result == 14

    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    result = do_algebra(operator, operand)
    assert result == 9

    operator = ['-', '*', '+']
    operand = [5, 2, 3, 4]
    result = do_algebra(operator, operand)
    assert result == 11

    operator = ['*', '//', '+']
    operand = [10, 2, 3, 4]
    result = do_algebra(operator, operand)
    assert result == 14

    operator = ['**', '//', '+']
    operand = [10, 2, 3, 4]
    result = do_algebra(operator, operand)
    assert result == 14

    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    result = do_algebra(operator, operand)
    assert result == 9

    operator = ['-', '*', '+']
    operand = [5, 2, 3, 4]
    result = do_algebra(operator, operand)
    assert result == 11

    operator = ['*', '//', '+']
    operand = [10, 2, 3, 4]
    result = do_algebra(operator, operand)
    assert result == 14

    operator = ['**', '//', '+']
    operand = [