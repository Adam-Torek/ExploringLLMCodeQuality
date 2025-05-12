"""
Write a function to check if a dictionary is empty
assert my_dict({10})==False
"""
def is_empty_dict(d):
    if len(d)==0:
        return True
    else:
        return False

# Test cases
print(is_empty_dict({})) # True
print(is_empty_dict({10: 20})) # False
print(is_empty_dict({})) # True
print(is_empty_dict({1: 2, 3: 4, 5: 6})) # False
print(is_empty_dict({})) # True
print(is_empty_dict({1: 2, 3: 4, 5: 6, 7: 8})) # False
print(is_empty_dict({1: 2, 3: 4, 5: 6, 7: 8, 9: 10})) # False
print(is_empty_dict({1: 2, 3: 4, 5: 6, 7: 8, 9: 10, 11: 12})) # False
print(is_empty_dict({1: 2, 3: 4, 5: 6, 7: 8, 9: 10, 11: 12, 13: 14})) # False
print(is_empty_dict({1: 2, 3: 4, 5: 6, 7: 8, 9: 10, 11: 12, 13: 14, 15: 16})) # False
print(is_empty_dict({1: 2, 3: 4, 5: 6, 7: 8, 9: 10, 11: 12, 13: 14, 15: 16, 17: 18})) # False
print(is_empty_dict({1: 2, 3: 4, 5: 6, 7: 8, 9: 10, 11: 12, 13: 14, 15: 16, 17: 18, 19: 20})) # False
print(is_empty_dict({1: 2, 3: 4, 5: 6, 7: 8, 9: 10, 11: 12, 13: 14, 15: 16, 17: 18, 19: 20, 21: 22})) # False
print(is_empty_dict({1: 2, 3: 4, 5: 6, 7: 8, 9: 10, 11: 12, 13: 14, 15: 16, 17: 18, 19: 20, 21: 22, 23: 24}) # False
print(is_empty_dict({1: 2, 3: 4, 5: 6, 7: 8, 9: 10, 11: 12, 13: 14, 15: 16, 17: 18, 19: 20, 21: 22, 23: 24, 25: 26}) # False
print(is_empty_dict({1: 2, 3: 4, 5: 6, 7: 8, 9: 10, 11: 12, 13: 14, 15: 16, 17: 18, 19: 20, 21: 22, 23: 24, 25: 26, 27: 28}) # False
print(is_empty_dict({1: 2, 3: 4, 5: 6, 7: 8,