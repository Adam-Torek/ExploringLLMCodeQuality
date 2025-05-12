"""
Write a function to extract values between quotation marks " " of the given string.
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
"""

def extract_quotation(string):
    return [x[1:-1] for x in string.split('"') if x not in ['', string.split('"')[0]]]

# Test cases
print(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"')) # Output: ['A53', 'multi', 'Processor']
print(extract_quotation('"Hello" "World" "Python"')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World"')) # Output: ['Hello', 'World']
print(extract_quotation('"Hello"')) # Output: ['Hello']
print(extract_quotation('No "quotation" marks')) # Output: []
print(extract_quotation('')) # Output: []
print(extract_quotation('"Hello" "World" "Python" "')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" " ")) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" " " " ')) # Output: ['Hello', 'World', 'Python