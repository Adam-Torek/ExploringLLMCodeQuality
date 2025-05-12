"""
Write a function to extract values between quotation marks " " of the given string.
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
"""

def extract_quotation(string):
    """
    Extract values between quotation marks " " of the given string.
    """
    return string.split('"')[1:-1]