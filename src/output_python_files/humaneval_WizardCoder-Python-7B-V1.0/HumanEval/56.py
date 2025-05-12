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
    return len(stack) == 0


# Test cases
print(correct_bracketing("<")) # False
print(correct_bracketing("<>")) # True
print(correct_bracketing("<<><>>")) # True
print(correct_bracketing("><<>")) # False


# Time complexity: O(n)
# Space complexity: O(n)

# Efficient solution

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
    return len(stack) == 0

# Test cases
print(correct_bracketing("<")) # False
print(correct_bracketing("<>")) # True
print(correct_bracketing("<<><>>")) # True
print(correct_bracketing("><<>")) # False

# Time complexity: O(n)
# Space complexity: O(n)

# Optimized solution

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
    count = 0
    for b in brackets:
        if b == "<":
            count += 1
        elif b == ">":
            count -= 1
        if count < 0:
            return False
    return count == 0

# Test cases
print(correct_bracketing("<")) # False
print(correct_bracketing("<>")) # True
print(correct_bracketing("<<><>>")) # True
print(correct_bracketing("><<>")) # False

# Time complexity: O(n)
# Space complexity: O(1)

# Another optimized solution

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
    count = 0
    for b in brackets:
        if b == "<":
            count += 1
        elif b == ">":
            count -= 1
            if count < 0:
                return False
    return count == 0

# Test cases
print(correct_bracketing("<")) # False
print(correct_bracketing("<>")) # True
print(correct_bracketing("<<><>>")) # True
print(correct_bracketing("><<>")) # False

# Time complexity: O(n)
# Space complexity: O(1)

#