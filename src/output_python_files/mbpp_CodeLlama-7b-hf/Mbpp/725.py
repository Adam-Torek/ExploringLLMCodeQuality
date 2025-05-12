"""
Write a function to extract values between quotation marks " " of the given string.
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
"""


def extract_quotation(string):
    """
    :param string: string to extract values from
    :return: list of values between quotation marks
    """
    result = []
    for i in range(len(string)):
        if string[i] == '"':
            if string[i + 1] == '"':
                result.append(string[i + 2:i + 3])
                i += 2
            else:
                result.append(string[i + 1:string.find('"', i + 1)])
                i = string.find('"', i + 1)
    return result


if __name__ == '__main__':
    print(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'))
    print(extract_quotation('"A53" Based "multi" tasking "Processor"'))
    print(extract_quotation('"A53" Based "multi" tasking "Processor" "A57"'))
    print(extract_quotation('"A53" Based "multi" tasking "Processor" "A57" "A53"'))
    print(extract_quotation('"A53" Based "multi" tasking "Processor" "A57" "A53" "A57"'))
    print(extract_quotation('"A53" Based "multi" tasking "Processor" "A57" "A53" "A57" "A53"'))
    print(extract_quotation('"A53" Based "multi" tasking "Processor" "A57" "A53" "A57" "A53" "A57"'))
    print(extract_quotation('"A53" Based "multi" tasking "Processor" "A57" "A53" "A57" "A53" "A57" "A53"'))
    print(extract_quotation('"A53" Based "multi" tasking "Processor" "A57" "A53" "A57" "A53" "A57" "A53" "A57"'))
    print(extract_quotation('"A53" Based "multi" tasking "Processor" "A57" "A53" "A57" "A53" "A57" "A53" "A57" "A53"'))
    print(extract_quotation('"A53" Based "multi" tasking "Processor" "A57" "A53" "A57" "A53" "A57" "A53" "A57" "A53" "A57"'))
    print(extract_quotation('"A53" Based "multi" tasking "Processor" "A57" "A53" "A57" "A53" "A57" "A53" "A57" "A53" "A57" "A53"'))
    print(extract_quotation('"A53" Based "multi" tasking "Processor" "A57" "A53" "A57" "A53" "A57" "A53" "A57" "A53" "A57" "A53" "A57"'))
    print(extract_quotation('"A53" Based "multi" tasking "Processor" "A57" "A53" "A57" "A53" "A57" "A53" "A57" "A53" "A