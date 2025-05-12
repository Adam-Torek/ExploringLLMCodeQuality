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
        if bracket == ">":
            if not stack or stack.pop() != "<":
                return False
        else:
            stack.append(bracket)
    return not stack


def test_correct_bracketing():
    """
    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    assert correct_bracketing("<") == False
    assert correct_bracketing("<>") == True
    assert correct_bracketing("<<><>>") == True
    assert correct_bracketing("><<>") == False


if __name__ == "__main__":
    test_correct_bracketing()