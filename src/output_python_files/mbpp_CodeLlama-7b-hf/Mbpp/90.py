"""
Write a python function to find the length of the longest word.
assert len_log(["python","PHP","bigdata"]) == 7
"""


def len_log(arr):
    """
    :param arr: list of strings
    :return: int
    """
    max_len = 0
    for i in arr:
        if len(i) > max_len:
            max_len = len(i)
    return max_len


if __name__ == '__main__':
    print(len_log(["python", "PHP", "bigdata"]))
    print(len_log(["python", "PHP", "bigdata", "java"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++", "c#"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++", "c#", "c++"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++", "c#", "c++", "c#"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++", "c#", "c++", "c#", "c++"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++", "c#", "c++", "c#", "c++", "c#"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++", "c#", "c++", "c#", "c++", "c#", "c++"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++", "c#", "c++", "c#", "c++", "c#", "c++", "c#"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++", "c#", "c++", "c#", "c++", "c#", "c++", "c#", "c++"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++", "c#", "c++", "c#", "c++", "c#", "c++", "c#", "c++", "c#"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++", "c#", "c++", "c#", "c++", "c#", "c++", "c#", "c++", "c#", "c++"]))
    print(len_log(["python", "PHP", "bigdata", "java", "c++", "c#", "c", "c#", "c++", "c#", "c++", "c#", "c++", "c#", "c++