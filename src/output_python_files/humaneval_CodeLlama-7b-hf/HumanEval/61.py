def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0


def correct_bracketing_recursive(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing_recursive("(")
    False
    >>> correct_bracketing_recursive("()")
    True
    >>> correct_bracketing_recursive("(()())")
    True
    >>> correct_bracketing_recursive(")(()")
    False
    """
    if len(brackets) == 0:
        return True
    elif len(brackets) == 1:
        return False
    elif brackets[0] == "(":
        return correct_bracketing_recursive(brackets[1:])
    elif brackets[0] == ")":
        return False
    else:
        return correct_bracketing_recursive(brackets[1:])


def correct_bracketing_iterative(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing_iterative("(")
    False
    >>> correct_bracketing_iterative("()")
    True
    >>> correct_bracketing_iterative("(()())")
    True
    >>> correct_bracketing_iterative(")(()")
    False
    """
    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        elif len(stack) == 0:
            return False
        else:
            stack.pop()
    return len(stack) == 0


def correct_bracketing_iterative_2(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing_iterative_2("(")
    False
    >>> correct_bracketing_iterative_2("()")
    True
    >>> correct_bracketing_iterative_2("(()())")
    True
    >>> correct_bracketing_iterative_2(")(()")
    False
    """
    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        elif len(stack) == 0:
            return False
        else:
            stack.pop()
    return len(stack) == 0


def correct_bracketing_iterative_3(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing_iterative_3("(")
    False
    >>> correct_bracketing_iterative_3("()")
    True
    >>> correct_bracketing_iterative_3("(()())")
    True
    >>> correct_bracketing_iterative_3(")(()")
    False
    """
    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        elif len(stack) == 0:
            return False