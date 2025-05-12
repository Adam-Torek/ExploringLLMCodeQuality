"""
Write a function to remove uppercase substrings from a given string.
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
"""


def remove_uppercase(string):
    """
    Remove uppercase substrings from a given string.
    :param string: string to remove uppercase substrings from
    :return: string without uppercase substrings
    """
    result = ''
    for i in range(len(string)):
        if i == 0:
            result += string[i].lower()
        elif string[i].islower():
            result += string[i]
        else:
            result += string[i].lower()
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
    print(remove_uppercase('cAstyoUrFavoRit