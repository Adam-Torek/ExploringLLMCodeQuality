"""
Write a function to check if a dictionary is empty
assert my_dict({10})==False
"""
def is_empty_dict(dict_obj):
    if len(dict_obj) == 0:
        return True
    else:
        return False

# Test cases
print(is_empty_dict({})) # True
print(is_empty_dict({10: 20})) # False
print(is_empty_dict({})) # True
print(is_empty_dict({10: 20, 30: 40})) # False
print(is_empty_dict({})) # True
print(is_empty_dict({10: 20, 30: 40, "name": "John", "age": 30})) # False
print(is_empty_dict({})) # True
print(is_empty_dict({10: 20, 30: 40, "name": "John", "age": 30, "city": "New York"})) # False
print(is_empty_dict({})) # True
print(is_empty_dict({10: 20, 30: 40, "name": "John", "age": 30, "city": "New York", "country": "USA"})) # False
print(is_empty_dict({})) # True
print(is_empty_dict({10: 20, 30: 40, "name": "John", "age": 30, "city": "New York", "country": "USA", "occupation": "Engineer"})) # False
print(is_empty_dict({})) # True
print(is_empty_dict({10: 20, 30: 40, "name": "John", "age": 30, "city": "New York", "country": "USA", "occupation": "Engineer", "salary": 500000})) # False
print(is_empty_dict({})) # True
print(is_empty_dict({10: 20, 30: 40, "name": "John", "age": 30, "city": "New York", "country": "USA", "occupation": "Engineer", "salary": 500000, "car": "BMW"})) # False
print(is_empty_dict({})) # True
print(is_empty_dict({10: 20, 30: 40, "name": "John", "age": 30, "city": "New York", "country": "USA", "occupation": "Engineer", "salary": 50000, "car": "BMW", "pet": "Dog"})) # False
print(is_empty_dict({})) # True
print(is_empty_dict({10: 20, 30: 40, "name": "John", "age": 30, "city": "New York", "country": "USA", "occupation": "Engineer", "salary": 5000, "car": "BMW", "pet": "Dog", "hobbies": ["Reading", "Traveling"]}) # False
print(is_empty_dict({})) # True
print(is_empty_dict({10: 20, 30: 40, "name": "John", "age": 30, "city": "New York", "country": "USA", "occupation": "Engineer", "salary": 500, "car": "BMW", "pet": "Dog", "hobbies": ["Reading", "Traveling"], "friends": ["Alice", "Bob"]})) # False
print(is_empty_dict({})) # True
print(is_empty_dict({10: 20, 30: 40, "name": "John", "age": 30, "city": "New York", "country": "USA", "occupation": "Engineer", "salary": 500, "car": "BMW", "pet": "Dog", "hobbies": ["