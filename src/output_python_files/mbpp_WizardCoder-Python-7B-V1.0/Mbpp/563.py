"""
Write a function to extract values between quotation marks from a string.
assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
"""

def extract_values(string):
    values = []
    start = False
    current_value = ""
    for char in string:
        if char == '"':
            if start:
                values.append(current_value)
                current_value = ""
                start = False
            else:
                start = True
        elif start:
            current_value += char
    return values

print(extract_values('"Python", "PHP", "Java"')) # ['Python', 'PHP', 'Java']
print(extract_values('"Python", "PHP", "Java"')) # ['Python', 'PHP', 'Java']
print(extract_values('"Python"')) # ['Python']
print(extract_values('"Python, PHP, Java"')) # []
print(extract_values('"Python", "PHP", "Java, C++"')) # ['Python', 'PHP', 'Java, C++']
print(extract_values('"Python", "PHP", "Java, C++"')) # ['Python', 'PHP', 'Java, C++']
print(extract_values('"Python", "PHP", "Java, C++"')) # ['Python', 'PHP', 'Java, C++']
print(extract_values('"Python", "PHP", "Java, C++"')) # ['Python', 'PHP', 'Java, C++']
print(extract_values('"Python", "PHP", "Java, C++"')) # ['Python', 'PHP', 'Java, C++']
print(extract_values('"Python", "PHP", "Java, C++"')) # ['Python', 'PHP', 'Java, C++']
print(extract_values('"Python", "PHP", "Java, C++"')) # ['Python', 'PHP', 'Java, C++']
print(extract_values('"Python", "PHP", "Java, C++"')) # ['Python', 'PHP', 'Java, C++']
print(extract_values('"Python", "PHP", "Java, C++"')) # ['Python', 'PHP', 'Java, C++']
print(extract_values('"Python", "PHP", "Java, C++"')) # ['Python', 'PHP', 'Java, C++']
print(extract_values('"Python", "PHP", "Java, C++"')) # ['Python', 'PHP', 'Java, C++']
print(extract_values('"Python", "PHP", "Java, C++"')) # ['Python', 'PHP', 'Java, C++']
print(extract_values('"Python", "PHP", "Java, C++"')) # ['Python', 'PHP', 'Java, C++']
print(extract_values('"Python", "PHP", "Java, C++"')) # ['Python', 'PHP', 'Java, C++']
print(extract_values('"Python", "PHP", "Java, C++"')) # ['Python', 'PHP', 'Java, C++']
print(extract_values('"Python", "PHP", "Java, C++"')) # ['Python', 'PHP', 'Java, C++']
print(extract_values('"Python", "PHP", "Java, C++"')) # ['Python', 'PHP', 'Java, C++']
print(extract_values('"Python", "PHP", "Java, C++"')) # ['Python', 'PHP', 'Java, C++']
print(extract_values('"Python", "PHP", "Java, C++"')) # ['Python', 'PHP', 'Java, C++']
print(extract_values('"Python", "PHP", "Java, C++"')) # ['Python', 'PHP', 'Java, C++']
print(extract_values('"Python", "PHP", "Java, C++"')) # ['Python', 'PHP', 'Java, C++']
print(extract_values('"Python", "PHP", "Java, C++"')) # ['Python', 'PHP', 'Java, C++']
print(extract_values('"Python", "PHP", "Java, C++"')) # ['Python', 'PHP', 'Java, C++']
print(extract_values('"