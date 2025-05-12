"""
Write a function to remove the parenthesis and what is inbetween them from a string.
assert remove_parenthesis(["python (chrome)"])==("python")
"""


def remove_parenthesis(string):
    """
    Remove the parenthesis and what is inbetween them from a string.
    :param string: list of strings
    :return: string without parenthesis
    """
    return ''.join(string).replace('(', '').replace(')', '')


if __name__ == '__main__':
    print(remove_parenthesis(["python (chrome)"