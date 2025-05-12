"""
Write a function to extract values between quotation marks from a string.
assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
"""

def extract_values(string):
    """
    Extract values between quotation marks from a string.
    """
    values = []
    for item in string.split(','):
        if '"' in item:
            values.append(item.strip('"'))
    return values

# assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']