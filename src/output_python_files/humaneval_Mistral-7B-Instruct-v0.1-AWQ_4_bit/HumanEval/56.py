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
    test_cases = [
        ("<", False),
        (">", False),
        ("<<", False),
        (">>", False),
        ("<<><>>", True),
        ("><<>", False),
        ("<<>>>", True),
        ("<<<>>>", False),
        ("<<<<<<<<>>>>>>>>", True),
    ]
    for brackets, expected in test_cases:
        assert correct_bracketing(brackets) == expected


if __name__ == "__main__":
    test_correct_bracketing()