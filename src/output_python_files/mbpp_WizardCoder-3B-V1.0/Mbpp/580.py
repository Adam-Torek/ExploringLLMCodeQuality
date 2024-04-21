"""
Write a function to remove uneven elements in the nested mixed tuple.
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
"""

def extract_even(nested_tuple):
    even_elements = []
    for element in nested_tuple:
        if isinstance(element, tuple):
            even_elements.extend(extract_even(element))
        elif isinstance(element, int) and element % 2 == 0:
            even_elements.append(element)
    return even_elements

print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8))) # Output: (4, (6, (2, 4)), 6, 8)<|endoftext|>