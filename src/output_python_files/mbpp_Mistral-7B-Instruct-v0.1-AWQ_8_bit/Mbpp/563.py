"""
Write a function to extract values between quotation marks from a string.
assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
"""

def extract_values(s):
    """
    Extract values between quotation marks from a string.
    """
    return [x.strip() for x in s.split(",") if x.strip() == x.strip('"')]

# assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']