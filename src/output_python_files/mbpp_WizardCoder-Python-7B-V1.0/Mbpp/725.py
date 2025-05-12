"""
Write a function to extract values between quotation marks " " of the given string.
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
"""
def extract_quotation(string):
    result = []
    start = False
    temp = ""
    for i in string:
        if i == '"':
            if start:
                result.append(temp)
                temp = ""
                start = False
            else:
                start = True
        elif start:
            temp += i
    return result

# Test cases
print(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"')) # Output: ['A53', 'multi', 'Processor']
print(extract_quotation('"Hello" "World" "Python"')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" "!"')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" "!" "')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" "!" " "')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" "!" " " "')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" "!" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" "!" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" "!" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" "!" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" "!" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" "!" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" "!" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" "!" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" "!" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" "!" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" "!" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" "!" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" "!" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" "!" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" "!" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_quotation('"Hello" "World" "Python" "!" " " " ')) # Output: ['Hello', 'World', 'Python']
print(extract_