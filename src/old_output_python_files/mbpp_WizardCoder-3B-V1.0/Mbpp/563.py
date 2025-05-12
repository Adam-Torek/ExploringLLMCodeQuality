"""
Write a function to extract values between quotation marks from a string.
assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
"""

def extract_values(string):
    values = []
    in_quotes = False
    current_value = ""
    for char in string:
        if char == '"' and not in_quotes:
            in_quotes = True
        elif char == '"' and in_quotes:
            values.append(current_value)
            current_value = ""
            in_quotes = False
        elif char == ',' and not in_quotes:
            values.append(current_value)
            current_value = ""
        elif char!= ',' and not in_quotes:
            current_value += char
    if current_value:
        values.append(current_value)
    return values

assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']<|endoftext|>