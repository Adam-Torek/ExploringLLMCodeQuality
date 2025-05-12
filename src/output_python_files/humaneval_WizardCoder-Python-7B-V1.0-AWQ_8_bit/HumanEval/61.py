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
    for b in brackets:
        if b == "(":
            stack.append(b)
        elif b == ")":
            if not stack:
                return False
            stack.pop()
    return not stack


# Test cases
print(correct_bracketing("()")) # True
print(correct_bracketing("(()())")) # True
print(correct_bracketing(")(()")) # False
print(correct_bracketing(")(")) # False


# Time complexity: O(n)
# Space complexity: O(n)


# Alternative solution using recursion

def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())
    True
    >>> correct_bracketing(")(()")
    False
    """
    def helper(s, i):
        if i == len(s):
            return True
        if s[i] == "(":
            return helper(s, i+1) and s[i+1] == ")"
        elif s[i] == ")":
            return False
        else:
            return False

    return helper(brackets, 0)

# Test cases
print(correct_bracketing("()")) # True
print(correct_bracketing("(()())") # True
print(correct_bracketing(")(()") # False

# Time complexity: O(n)
# Space complexity: O(n)

# Alternative solution using stack
def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())
    True
    >>> correct_bracketing(")(()")
    False
    """
    stack = []
    for b in brackets:
        if b == "(":
            stack.append(b)
        elif b == ")":
            if not stack:
                return False
            stack.pop()
    return not stack

# Test cases
print(correct_bracketing("()")) # True
print(correct_bracketing("(()())") # True
print(correct_bracketing(")(()") # False

# Time complexity: O(n)
# Space complexity: O(n)

# Alternative solution using stack and index pointers
def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())
    True
    >>> correct_bracketing(")(()")
    False
    """
    stack = []
    i = 0
    while i < len(brackets):
        if brackets[i] == "(":
            stack.append(i)
        elif brackets[i] == ")":
            if not stack:
                return False
            stack.pop()
        i += 1
    return not stack

# Test cases
print(correct_bracketing("()")) # True
print(correct_bracketing("(()())") # True
print(correct_bracketing(")(()") # False

# Time complexity: O(n)
# Space complexity: O(n)

# Alternative solution using index pointers
def correct_bracketing(brackets: str):
    """ brackets is a string