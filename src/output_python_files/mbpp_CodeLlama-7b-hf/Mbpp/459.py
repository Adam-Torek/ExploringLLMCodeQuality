"""
Write a function to remove uppercase substrings from a given string.
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
"""


def remove_uppercase(string):
    """
    :param string: string
    :return: string without uppercase substrings
    """
    result = ''
    for i in range(len(string)):
        if string[i].islower():
            result += string[i]
        elif string[i].isupper():
            if i == 0:
                result += string[i].lower()
            elif string[i - 1].islower():
                result += string[i].lower()
            else:
                result += string[i]
    return result


if __name__ == '__main__':
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
    print(remove_uppercase('cAstyoUr