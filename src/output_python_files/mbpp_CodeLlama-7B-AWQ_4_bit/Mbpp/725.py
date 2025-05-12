"""
Write a function to extract values between quotation marks " " of the given string.
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
"""


def extract_quotation(string):
    """
    :param string: str
    :return: list
    """
    result = []
    for i in range(len(string)):
        if string[i] == '"':
            result.append(string[i + 1:string.index('"', i + 1)])
    return result


if __name__ == '__main__':
    print(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'))
    print(extract_quotation('"A53" Based "multi" tasking "Processor"'))
    print(extract_quotation('"A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor"'))
    print(extract_quotation('"A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor"'))
    print(extract_quotation('"A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor"'))
    print(extract_quotation('"A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor"'))
    print(extract_quotation('"A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor"'))
    print(extract_quotation('"A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor"'))
    print(extract_quotation('"A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor"'))
    print(extract_quotation('"A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor" "A53" Based "multi" tasking "Processor"'))
    print(extract_quotation('"A53" Based "multi" tasking "Processor" "A53" Based