"""
Write a function to check if a dictionary is empty
assert my_dict({10})==False
"""

def is_empty_dict(d):
    return len(d) == 0

# Test cases
print(is_empty_dict({})) # True
print(is_empty_dict({10: 20})) # False
print(is_empty_dict({})) # True
print(is_empty_dict({1: 2, 3: 4, 5: 6})) # False
print(is_empty_dict({})) # True
print(is_empty_dict({"a": "b", "c": "d"})) # False
print(is_empty_dict({})) # True
print(is_empty_dict({"a": 1, "b": 2, "c": 3})) # False
print(is_empty_dict({})) # True
print(is_empty_dict({"x": [1, 2, 3]})) # False
print(is_empty_dict({})) # True
print(is_empty_dict({"x": {"y": 1, "z": 2})) # False
print(is_empty_dict({}) # True
print(is_empty_dict({"x": (1, 2, 3)}) # False
print(is_empty_dict({}) # True
print(is_empty_dict({"x": "hello"})) # False
print(is_empty_dict({}) # True
print(is_empty_dict({"x": 10}) # False
print(is_empty_dict({})) # True
print(is_empty_dict({"x": 10.5} # False
print(is_empty_dict({})) # True
print(is_empty_dict({"x": None} # False
print(is_empty_dict({})) # True
print(is_empty_dict({"x": "hello"} # False
print(is_empty_dict({})) # True
print(is_empty_dict({"x": []} # False
print(is_empty_dict({})) # True
print(is_empty_dict({"x": {}} # False
print(is_empty_dict({})) # True
print(is_empty_dict({"x": {1, 2, 3, 4, 5} # False
print(is_empty_dict({})) # True
print(is_empty_dict({"x": {1: 2, 3: 4, 5: 6} # False
print(is_empty_dict({})) # True
print(is_empty_dict({"x": {"y": [1, 2, 3]} # False
print(is_empty_dict({})) # True
print(is_empty_dict({"x": {"y": {"z": 1, "w": 2} # False
print(is_empty_dict({})) # True
print(is_empty_dict({"x": {"y": {"z": {"a": 1, "b": 2} # False
print(is_empty_dict({})) # True
print(is_empty_dict({"x": {"y": {"z": {"a": [1, 2, 3]} # False
print(is_empty_dict({})) # True
print(is_empty_dict({"x": {"y": {"z": {"a": (1, 2, 3) # False
print(is_empty_dict({})) # True
print(is_empty_dict({"x": {"y": {"z": {"a": None} # False
print(is_empty_dict({})) # True
print(is_empty_dict({"x": {"y": {"z": {"a": "hello"} # False
print(is_empty_dict({})) # True
print(is_empty_dict({"x": {"y": {"z": {"a": []} # False
print(is_empty_dict({})) # True
print(is_empty_dict({"x": {"y": {"z": {"a": {}} # False
print(is_empty_dict({})) # True
print(is_empty_dict({"x": {"y": {"z": {"a": {1, 2, 3} # False
print(is_empty_dict({})) # True
print(is_empty_dict({