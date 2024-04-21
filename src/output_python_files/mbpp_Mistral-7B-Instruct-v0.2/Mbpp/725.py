"""
Write a function to extract values between quotation marks " " of the given string.
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
"""
import re

def extract_quotation(string):
    """
    Extract values between quotation marks " " of the given string.
    """
    pattern = r'(?<=")[^"]+(?=")'
    return re.findall(pattern, string)

assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']</s>