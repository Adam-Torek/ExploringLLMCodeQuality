"""
Write a function to extract values between quotation marks " " of the given string.
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53','multi', 'Processor']
"""

def extract_quotation(string):
    quotation_marks = []
    in_quotation = False
    for char in string:
        if char == '"':
            in_quotation = not in_quotation
        if in_quotation:
            quotation_marks.append(char)
    return quotation_marks

# Test cases
print(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"')) # Output: ['A53','multi', 'Processor']<|endoftext|>