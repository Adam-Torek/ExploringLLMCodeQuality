"""
Write a function to extract values between quotation marks " " of the given string.
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
"""
def extract_quotation(string):
    """
    Extracts values between quotation marks " " from the given string.
    :param string: str
    :return: list
    """
    return re.findall(r'"[^"]+"', string)

import re

assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']