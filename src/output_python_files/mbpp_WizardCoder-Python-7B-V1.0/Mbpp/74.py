"""
Write a function to check whether it follows the sequence given in the patterns array.
assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
"""

def is_samepatterns(patterns, letters):
    if len(patterns) != len(letters):
        return False
    for i in range(len(patterns)):
        if patterns[i] == "red":
            if letters[i] != "a":
                return False
        elif patterns[i] == "green":
            if letters[i] != "b":
                return False
        elif patterns[i] == "blue":
            if letters[i] != "c":
                return False
    return True

print(is_samepatterns(["red","green","green"], ["a", "b", "b"])) # True
print(is_samepatterns(["red","green","blue"], ["a", "b", "c"])) # True
print(is_samepatterns(["red","green","blue"], ["a", "b", "a"])) # False
print(is_samepatterns(["red","green","blue"], ["a", "b", "c", "d"])) # False
print(is_samepatterns(["red","green","blue"], ["a", "b", "c", "d", "e"])) # False
print(is_samepatterns(["red","green","blue"], ["a", "b", "c", "d", "e", "f"])) # False
print(is_samepatterns(["red","green","blue"], ["a", "b", "c", "d", "e", "f", "g"])) # False
print(is_samepatterns(["red","green","blue"], ["a", "b", "c", "d", "e", "f", "g", "h"])) # False
print(is_samepatterns(["red","green","blue"], ["a", "b", "c", "d", "e", "f", "g", "h", "i"])) # False
print(is_samepatterns(["red","green","blue"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])) # False
print(is_samepatterns(["red","green","blue"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"])) # False
print(is_samepatterns(["red","green","blue"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"])) # False
print(is_samepatterns(["red","green","blue"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"])) # False
print(is_samepatterns(["red","green","blue"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"])) # False
print(is_samepatterns(["red","green","blue"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"])) # False
print(is_samepatterns(["red","green","blue"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"])) # False
print(is_samepatterns(["red","green","blue"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q"])) # False
print(is_samepatterns(["red","green","blue"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",