"""
Write a function to extract values between quotation marks from a string.
assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
"""


def extract_values(string):
    """
    :param string: string
    :return: list of values between quotation marks
    """
    return [value.strip('"') for value in string.split(',')]


if __name__ == '__main__':
    print(extract_values('"Python", "PHP", "Java"'))
    print(extract_values('"Python", "PHP", "Java"', 'Python'))
    print(extract_values('"Python", "PHP", "Java"', 'Python', 'PHP'))
    print(extract_values('"Python", "PHP", "Java"', 'Python', 'PHP', 'Java'))
    print(extract_values('"Python", "PHP", "Java"', 'Python', 'PHP', 'Java', 'C++'))
    print(extract_values('"Python", "PHP", "Java"', 'Python', 'PHP', 'Java', 'C++', 'C#'))
    print(extract_values('"Python", "PHP", "Java"', 'Python', 'PHP', 'Java', 'C++', 'C#', 'Ruby'))
    print(extract_values('"Python", "PHP", "Java"', 'Python', 'PHP', 'Java', 'C++', 'C#', 'Ruby', 'Go'))
    print(extract_values('"Python", "PHP", "Java"', 'Python', 'PHP', 'Java', 'C++', 'C#', 'Ruby', 'Go', 'C'))
    print(extract_values('"Python", "PHP", "Java"', 'Python', 'PHP', 'Java', 'C++', 'C#', 'Ruby', 'Go', 'C', 'C#'))
    print(extract_values('"Python", "PHP", "Java"', 'Python', 'PHP', 'Java', 'C++', 'C#', 'Ruby', 'Go', 'C', 'C#', 'C++'))
    print(extract_values('"Python", "PHP", "Java"', 'Python', 'PHP', 'Java', 'C++', 'C#', 'Ruby', 'Go', 'C', 'C#', 'C++', 'C'))
    print(extract_values('"Python", "PHP", "Java"', 'Python', 'PHP', 'Java', 'C++', 'C#', 'Ruby', 'Go', 'C', 'C#', 'C++', 'C', 'C#'))
    print(extract_values('"Python", "PHP", "Java"', 'Python', 'PHP', 'Java', 'C++', 'C#', 'Ruby', 'Go', 'C', 'C#', 'C++', 'C', 'C#', 'C++'))
    print(extract_values('"Python", "PHP", "Java"', 'Python', 'PHP', 'Java', 'C++', 'C#', 'Ruby', 'Go', 'C', 'C#', 'C++', 'C', 'C#', 'C++', 'C#'))
    print(extract_values('"Python", "PHP", "Java"', 'Python', 'PHP', 'Java', 'C++', 'C#', 'Ruby', 'Go', 'C', 'C#', 'C++', 'C', 'C#', 'C++', 'C#', 'C++'))
    print(extract_values('"Python", "PHP", "Java"', 'Python', 'PHP', 'Java', 'C++', 'C#', 'Ruby', 'Go', 'C', 'C#', 'C++', 'C', 'C#', 'C++', 'C#', 'C++', 'C#'))
    print(extract_values('"Python", "PHP", "Java"', 'Python', 'PHP', 'Java', 'C++', 'C#', 'Ruby', 'Go', 'C', 'C#', 'C++', 'C', 'C#', 'C++', 'C#', 'C++', 'C#', 'C++'))
    print(extract_values('"Python", "PHP", "Java"', 'Python', 'PHP', 'Java', 'C++', 'C#', 'Ruby', 'Go', 'C', 'C#', 'C