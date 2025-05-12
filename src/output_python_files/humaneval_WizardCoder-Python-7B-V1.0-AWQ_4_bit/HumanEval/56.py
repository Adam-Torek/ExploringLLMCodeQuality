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


# Time Complexity: O(n)
# Space Complexity: O(n)


# Efficient Solution

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

# Time Complexity: O(n)
# Space Complexity: O(n)

# This solution is more efficient as it uses a stack to keep track of opening brackets and pops the last opening bracket when a closing bracket is encountered. If the stack is empty or the popped opening bracket is not the expected closing bracket, return False. If all opening brackets have a corresponding closing bracket, return True.

# Another solution is to use a counter variable to keep track of the number of opening brackets and closing brackets. If the counter is ever negative, return False. If the counter is 0 at the end, return True.

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

# Time Complexity: O(n)
# Space Complexity: O(1)

# This solution uses a counter variable to keep track of the number of opening and closing brackets. If the counter is ever negative, return False. If the counter is 0 at the end, return True. This solution is more efficient as it does not require a stack.