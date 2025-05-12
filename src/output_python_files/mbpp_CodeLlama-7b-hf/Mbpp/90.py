"""
Write a python function to find the length of the longest word.
assert len_log(["python","PHP","bigdata"]) == 7
"""


def len_log(lst):
    """
    :param lst: list of strings
    :return: length of the longest word
    """
    return max(map(len, lst))


if __name__ == '__main__':
    print(len_log(["python", "PHP", "bigdata"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++", "c#"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++", "c#", "c"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++", "c#", "c", "c#"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++", "c#", "c", "c#", "c"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++", "c#", "c", "c#", "c", "c#"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++", "c#", "c", "c#", "c", "c#", "c"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++", "c#", "c", "c#", "c", "c#", "c", "c#"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++", "c#", "c", "c#", "c", "c#", "c", "c#", "c"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++", "c#", "c", "c#", "c", "c#", "c", "c#", "c", "c#"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++", "c#", "c", "c#", "c", "c#", "c", "c#", "c", "c#", "c"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++", "c#", "c", "c#", "c", "c#", "c", "c#", "c", "c#", "c", "c#"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++",