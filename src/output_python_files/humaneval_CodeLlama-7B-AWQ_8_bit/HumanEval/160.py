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
    # Your code here
    result = 0
    for i in range(len(operand)):
        if i == 0:
            result = operand[i]
        else:
            if operator[i - 1] == '+':
                result += operand[i]
            elif operator[i - 1] == '-':
                result -= operand[i]
            elif operator[i - 1] == '*':
                result *= operand[i]
            elif operator[i - 1] == '//':
                result //= operand[i]
            elif operator[i - 1] == '**':
                result **= operand[i]
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9, "1st example"
    assert do_algebra(['+', '*', '-'], [1, 2, 3, 4, 5]) == 15, "2nd example"
    assert do_algebra(['+', '*', '-'], [1, 2, 3, 4, 5, 6]) == 21, "3rd example"
    assert do_algebra(['+', '*', '-'], [1, 2, 3, 4, 5, 6, 7]) == 28, "4th example"
    assert do_algebra(['+', '*', '-'], [1, 2, 3, 4, 5, 6, 7, 8]) == 36, "5th example"
    assert do_algebra(['+', '*', '-'], [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45, "6th example"
    assert do_algebra(['+', '*', '-'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55, "7th example"
    assert do_algebra(['+', '*', '-'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 66, "8th example"
    assert do_algebra(['+', '*', '-'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 78, "9th example"
    assert do_algebra(['+', '*', '-'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 91, "10th example"
    assert do_algebra(['+', '*', '-'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 105, "11th example"