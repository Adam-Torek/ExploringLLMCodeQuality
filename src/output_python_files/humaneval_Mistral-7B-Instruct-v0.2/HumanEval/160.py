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
        raise ValueError("The length of operator and operand list must be equal except one")

    stack = []
    for i in range(len(operand)):
        stack.append(operand[i])
        if i < len(operator) and operator[i] != '':
            stack[-1] = apply_operator(stack.pop(), stack.pop(), operator[i])

    return stack[0]

def apply_operator(operand1, operand2, operator):
    """
    Given three arguments: two operands and an operator. Use the operator to apply the 
    operation on the two given operands and return the result.

    The basic algebra operations:
    Addition ( + )
    Subtraction ( - )
    Multiplication ( * )
    Floor division ( // )
    Exponentiation ( ** )

    Example:
    apply_operator(3, 4, '+')
    => 7

    apply_operator(3, 4, '*')
    => 12

    apply_operator(3, 4, '/')
    => 1.0

    apply_operator(3, 4, '//')
    => 1

    apply_operator(3, 4, '**')
    => 81

    """
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
    elif operator == '//':
        return int(operand1 / operand2)
    elif operator == '**':
        return operand1 ** operand2
    else:
        raise ValueError("Invalid operator")

if __name__ == "__main__":
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    result = do_algebra(operator, operand)
    print(result)</s>