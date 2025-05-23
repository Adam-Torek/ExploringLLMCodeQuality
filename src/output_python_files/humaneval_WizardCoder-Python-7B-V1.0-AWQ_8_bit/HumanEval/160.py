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
    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i+1]
        elif operator[i] == '-':
            result -= operand[i+1]
        elif operator[i] == '*':
            result *= operand[i+1]
        elif operator[i] == '//':
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
    return result



# Test cases
print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))  # Output: 9
print(do_algebra(['*', '//', '**'], [2, 3, 4, 5, 2])  # Output: 16
print(do_algebra(['+', '*', '**'], [2, 3, 4, 5, 2])  # Output: 32
print(do_algebra(['*', '//', '+'], [2, 3, 4, 5, 2])  # Output: 10
print(do_algebra(['*', '+', '**'], [2, 3, 4, 5, 2])  # Output: 32
print(do_algebra(['-', '*', '+'], [2, 3, 4, 5, 2])  # Output: -10
print(do_algebra(['*', '//', '-'], [2, 3, 4, 5, 2])  # Output: 8
print(do_algebra(['**', '+', '*'], [2, 3, 4, 5, 2])  # Output: 32
print(do_algebra(['**', '//', '-'], [2, 3, 4, 5, 2])  # Output: 16
print(do_algebra(['+', '**', '*'], [2, 3, 4, 5, 2])  # Output: 32
print(do_algebra(['-', '//', '+'], [2, 3, 4, 5, 2])  # Output: -10
print(do_algebra(['-', '*', '**'], [2, 3, 4, 5, 2])  # Output: -16
print(do_algebra(['+', '**', '-'], [2, 3, 4, 5, 2])  # Output: 32
print(do_algebra(['-', '//', '*'], [2, 3, 4, 5, 2])  # Output: -8
print(do_algebra(['**', '+', '-'], [2, 3, 4, 5, 2])  # Output: 32
print(do_algebra(['/', '*', '+'], [2, 3, 4, 5, 2])  # Output: 10
print(do_algebra(['/', '//', '**'], [2, 3, 4, 5, 2])  # Output: 16
print(do_algebra(['/', '+', '*'], [2, 3,