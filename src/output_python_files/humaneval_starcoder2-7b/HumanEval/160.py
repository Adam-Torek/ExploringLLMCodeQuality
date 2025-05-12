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

# +
# Test Cases

operator = ['+', '*', '-']
operand = [2, 3, 4, 5]

print(do_algebra(operator, operand))

operator = ['+', '*', '-']
operand = [2, 3, 4, 5, 6]

print(do_algebra(operator, operand))

operator = ['+', '*', '-']
operand = [2, 3, 4, 5, 6, 7]

print(do_algebra(operator, operand))

operator = ['+', '*', '-']
operand = [2, 3, 4, 5, 6, 7, 8]

print(do_algebra(operator, operand))

operator = ['+', '*', '-']
operand = [2, 3, 4, 5, 6, 7, 8, 9]

print(do_algebra(operator, operand))

operator = ['+', '*', '-']
operand = [2, 3, 4, 5, 6, 7, 8, 9, 10]

print(do_algebra(operator, operand))

operator = ['+', '*', '-']
operand = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(do_algebra(operator, operand))

operator = ['+', '*', '-']
operand = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(do_algebra(operator, operand))

operator = ['+', '*', '-']
operand = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(do_algebra(operator, operand))

operator = ['+', '*', '-']
operand = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(do_algebra(operator, operand))

operator = ['+', '*', '-']
operand = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(do_algebra(operator, operand))

operator = ['+', '*', '-']
operand = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

print(do_algebra(operator, operand))

operator = ['+', '*', '-']
operand = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

print(do_algebra(operator, operand))

operator = ['+', '*', '-']
operand = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

print(do_algebra(