"""
Write a function to check whether the given string starts and ends with the same character or not.
assert check_char("abba") == "Valid"
"""


def check_char(string):
    if string[0] == string[-1]:
        return "Valid"
    else:
        return "Invalid"


if __name__ == '__main__':
    print(check_char("abba"))
    print(check_char("abbaa"))
    print(check_char("abbaab"))
    print(check_char("abbaabba"))
    print(check_char("abbaabbaa"))
    print(check_char("abbaabbaab"))
    print(check_char("abbaabbaabba"))
    print(check_char("abbaabbaabbaa"))
    print(check_char("abbaabbaabbaab"))
    print(check_char("abbaabbaabbaabba"))
    print(check_char("abbaabbaabbaabbaa"))
    print(check_char("abbaabbaabbaabbaab"))
    print(check_char("abbaabbaabbaabbaabba"))
    print(check_char("abbaabbaabbaabbaabbaa"))
    print(check_char("abbaabbaabbaabbaabbaab"))
    print(check_char("abbaabbaabbaabbaabbaabba"))
    print(check_char("abbaabbaabbaabbaabbaabbaa"))
    print(check_char("abbaabbaabbaabbaabbaabbaab"))
    print(check_char("abbaabbaabbaabbaabbaabbaabba"))
    print(check_char("abbaabbaabbaabbaabbaabbaabbaa"))
    print(check_char("abbaabbaabbaabbaabbaabbaabbaab"))
    print(check_char("abbaabbaabbaabbaabbaabbaabbaabba"))
    print(check_char("abbaabbaabbaabbaabbaabbaabbaabbaa"))
    print(check_char("abbaabbaabbaabbaabbaabbaabbaabbaab"))
    print(check_char("abbaabbaabbaabbaabbaabbaabbaabbaabba"))
    print(check_char("abbaabbaabbaabbaabbaabbaabbaabbaabbaa"))
    print(check_char("abbaabbaabbaabbaabbaabbaabbaabbaabbaab"))
    print(check_char("abbaabbaabbaabbaabbaabbaabbaabbaabbaabba"))
    print(check_char("abbaabbaabbaabbaabbaabbaabbaabbaabbaabbaa"))
    print(check_char("abbaabbaabbaabbaabbaabbaabbaabbaabbaabbaab"))
    print(check_char("abbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabba"))
    print(check_char("abbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaa"))
    print(check_char("abbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaab"))
    print(check_char("abbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabba"))
    print(check_char("abbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaa"))
    print(check_char("abbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaab"))
    print(check_char("abbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabba"))
    print(check_char("abbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaa"))
    print(check_char("abbaabbaabbaabbaabbaabbaabbaabbaabbaabbaab