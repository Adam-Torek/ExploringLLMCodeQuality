def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


def correct_bracketing_2(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing_2("<")
    False
    >>> correct_bracketing_2("<>")
    True
    >>> correct_bracketing_2("<<><>>")
    True
    >>> correct_bracketing_2("><<>")
    False
    """
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


def correct_bracketing_3(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing_3("<")
    False
    >>> correct_bracketing_3("<>")
    True
    >>> correct_bracketing_3("<<><>>")
    True
    >>> correct_bracketing_3("><<>")
    False
    """
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


def correct_bracketing_4(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing_4("<")
    False
    >>> correct_bracketing_4("<>")
    True
    >>> correct_bracketing_4("<<><>>")
    True
    >>> correct_bracketing_4("><<>")
    False
    """
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


def correct_bracketing_5(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing_5("<")
    False
    >>> correct_bracketing_5("<>")
    True
    >>> correct_bracketing_5("<<><>>")
    True
    >>> correct_bracketing_5("><<>")
    False
    """
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


def correct_bracketing_6(bra