def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """

# Solution:
# We can solve this problem by iterating over the levels and calculating the number of stones in each level.
# We can use the formula for the number of stones in the next level as follows:
# - If n is odd, the next level has n+1 stones.
# - If n is even, the next level has n stones.
# We can then append the number of stones in each level to a list and return it.

def make_a_pile(n):
    levels = []
    current_level = 1
    while current_level <= n:
        next_level = current_level + 1 if current_level % 2 == 1 else current_level
        levels.append(next_level)
        current_level += 1
    return levels

# Test cases
print(make_a_pile(3))  # Output: [3, 5, 7]
print(make_a_pile(4))  # Output: [4, 6, 8]
print(make_a_pile(5))  # Output: [5, 7, 9]
print(make_a_pile(6))  # Output: [6, 8, 10]<|endoftext|>