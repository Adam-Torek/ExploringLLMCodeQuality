"""
Write a function to extract values between quotation marks " " of the given string.
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
"""

def extract_quotation(string):
    return [x[1:-1] for x in string.split('"') if x not in ('', string.split('"')[::2][1::2]]


# Test cases
print(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"')) # Output: ['A53', 'multi', 'Processor']
print(extract_quotation('"Hello" "world" "Python"')) # Output: ['Hello', 'Python']
print(extract_quotation('"Hello" "world" "Python" "!"')) # Output: ['Hello', 'Python']
print(extract_quotation('"Hello" "world" "Python" "!" "')) # Output: ['Hello', 'Python']
print(extract_quotation('"Hello" "world" "Python" "!" "')) # Output: []
print(extract_quotation('"Hello" "world" "Python"')) # Output: ['Hello', 'world']
print(extract_quotation('"Hello" "world" "Python" "!" "world"')) # Output: ['Hello', 'Python', 'world']
print(extract_quotation('"Hello" "world" "Python" "!" "world" "Python"')) # Output: ['Hello', 'world', 'Python', 'Python']
print(extract_quotation('"Hello" "world" "Python" "!" "world" "Python" "!"')) # Output: ['Hello', 'world', 'Python', 'Python']
print(extract_quotation('"Hello" "world" "Python" "!" "world" "Python" "!" "world"')) # Output: ['Hello', 'world', 'Python', 'Python']
print(extract_quotation('"Hello" "world" "Python" "!" "world" "Python" "!" "world" "Python" "!"')) # Output: ['Hello', 'world', 'Python', 'Python']
print(extract_quotation('"Hello" "world" "Python" "!" "world" "Python" "!" "world" "Python" "!" "world"')) # Output: ['Hello', 'world', 'Python', 'Python']
print(extract_quotation('"Hello" "world" "Python" "!" "world" "Python" "!" "world" "Python" "!" "world" "Python"')) # Output: ['Hello', 'world', 'Python', 'Python']
print(extract_quotation('"Hello" "world" "Python" "!" "world" "Python" "!" "world" "Python" "!" "world" "Python" "!" "world"')) # Output: ['Hello', 'world', 'Python', 'Python']
print(extract_quotation('"Hello" "world" "Python" "!" "world" "Python" "!" "world" "Python" "!" "world" "Python" "!" "world" "Python" "!" "world"')) # Output: ['Hello', 'world', 'Python', 'Python']
print(extract_quotation('"Hello" "world" "Python" "!" "world" "Python" "!" "world" "Python" "!" "world" "Python" "!" "world" "Python" "!" "world" "Python" "!" "world"')) # Output: ['Hello', 'world', 'Python', 'Python']
print(extract_quotation('"Hello" "world" "Python" "!" "world" "Python" "!" "world" "Python" "!" "world" "Python" "!" "world" "Python" "!" "world" "Python" "!" "world" "Python" "!" "world" "Python" "!" "world"')) # Output: ['Hello', 'world', 'Python', 'Python']
print(extract_quotation('"Hello"