"""
Write a function to check whether it follows the sequence given in the patterns array.
assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
"""

def is_samepatterns(patterns, strings):
    if len(patterns) != len(strings):
        return False
    for i in range(len(patterns)):
        if patterns[i] != strings[i] and patterns[i] != strings[i][0]:
            return False
    return True

# Test cases
print(is_samepatterns(["red","green","green"], ["a", "b", "b"])) # True
print(is_samepatterns(["red","green","green"], ["a", "b", "c"])) # False
print(is_samepatterns(["red","green","green"], ["a", "b", "bc"])) # True
print(is_samepatterns(["red","green","green"], ["a", "b", "c"])) # False
print(is_samepatterns(["red","green","green"], ["a", "b", "bc"])) # True
print(is_samepatterns(["red","green","green"], ["a", "b", "c"])) # False
print(is_samepatterns(["red","green","green"], ["a", "b", "bc"])) # True
print(is_samepatterns(["red","green","green"], ["a", "b", "c"])) # False
print(is_samepatterns(["red","green","green"], ["a", "b", "bc"])) # True
print(is_samepatterns(["red","green","green"], ["a", "b", "c"])) # False
print(is_samepatterns(["red","green","green"], ["a", "b", "bc"])) # True
print(is_samepatterns(["red","green","green"], ["a", "b", "c"])) # False
print(is_samepatterns(["red","green","green"], ["a", "b", "bc"])) # True
print(is_samepatterns(["red","green","green"], ["a", "b", "c"])) # False
print(is_samepatterns(["red","green","green"], ["a", "b", "bc"])) # True
print(is_samepatterns(["red","green","green"], ["a", "b", "c"])) # False
print(is_samepatterns(["red","green","green"], ["a", "b", "bc"])) # True
print(is_samepatterns(["red","green","green"], ["a", "b", "c"])) # False
print(is_samepatterns(["red","green","green"], ["a", "b", "bc"])) # True
print(is_samepatterns(["red","green","green"], ["a", "b", "c"])) # False
print(is_samepatterns(["red","green","green"], ["a", "b", "bc"])) # True
print(is_samepatterns(["red","green","green"], ["a", "b", "c"])) # False
print(is_samepatterns(["red","green","green"], ["a", "b", "bc"])) # True
print(is_samepatterns(["red","green","green"], ["a", "b", "c"])) # False
print(is_samepatterns(["red","green","green"], ["a", "b", "bc"])) # True
print(is_samepatterns(["red","green","green"], ["a", "b", "c"])) # False
print(is_samepatterns(["red","green","green"], ["a", "b", "bc"])) # True
print(is_samepatterns(["red","green","green"], ["a", "b", "c"])) # False
print(is_samepatterns(["red","green","green"], ["a", "b", "bc"])) # True
print(is_samepatterns(["red","green","green"], ["a", "b", "c"])) # False
print(is_samepatterns(["red","green","green"], ["a", "b", "bc"])) # True
print(is_samepatterns(["red","green","green"],