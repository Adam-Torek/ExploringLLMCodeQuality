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
    for b in brackets:
        if b == "<":
            stack.append(b)
        elif b == ">":
            if not stack:
                return False
            stack.pop()
    return not stack


# Test cases
print(correct_bracketing("<")) # False
print(correct_bracketing("<>")) # True
print(correct_bracketing("<<><>>")) # True
print(correct_bracketing("><<>")) # False


# Time complexity: O(n)
# Space complexity: O(n)


# Alternative solution using stack

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
    for b in brackets:
        if b == "<":
            stack.append(b)
        elif b == ">":
            if not stack or stack.pop() != "<":
                return False
    return not stack

# Test cases
print(correct_bracketing("<")) # False
print(correct_bracketing("<>")) # True
print(correct_bracketing("<<><>>")) # True
print(correct_bracketing("><<>")) # False

# Time complexity: O(n)
# Space complexity: O(n)

# Another alternative solution using recursion

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
    def helper(i, j):
        if i >= len(brackets) or j >= len(brackets):
            return True
        if brackets[i] == "<":
            if brackets[j] == ">":
                return helper(i+1, j-1)
        elif brackets[j] == "<":
            return helper(i, j+1)
        else:
            return False
    return helper(0, len(brackets)-1)

# Test cases
print(correct_bracketing("<")) # False
print(correct_bracketing("<>")) # True
print(correct_bracketing("<<><>>")) # True
print(correct_bracketing("><<>")) # False

# Time complexity: O(n)
# Space complexity: O(n)
# This solution uses recursion, but it's not recommended for large input sizes.