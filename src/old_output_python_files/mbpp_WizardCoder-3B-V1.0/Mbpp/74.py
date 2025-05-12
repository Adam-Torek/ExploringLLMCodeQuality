"""
Write a function to check whether it follows the sequence given in the patterns array.
assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
"""

def is_samepatterns(patterns1, patterns2):
    if len(patterns1)!= len(patterns2):
        return False
    for i in range(len(patterns1)):
        if patterns1[i]!= patterns2[i]:
            return False
    return True

# Test cases
print(is_samepatterns(["red","green","green"], ["a", "b", "b"])) # True
print(is_samepatterns(["red","green","green"], ["a", "b", "c"])) # False
print(is_samepatterns(["red","green","green"], ["a", "b"])) # False<|endoftext|>