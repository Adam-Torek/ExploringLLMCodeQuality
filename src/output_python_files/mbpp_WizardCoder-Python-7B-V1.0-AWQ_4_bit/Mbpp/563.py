"""
Write a function to extract values between quotation marks from a string.
assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
"""

def extract_values(string):
    return [x.strip('"') for x in string.split(',')]

print(extract_values('"Python", "PHP", "Java"')) # ['Python', 'PHP', 'Java']
print(extract_values('"Python", "PHP", "Java", "C#"')) # ['Python', 'PHP', 'Java', 'C#']
print(extract_values('"Python"')) # ['Python']
print(extract_values('"Python" , "Java"')) # ['Python', 'Java']
print(extract_values('"Python", "Java"')) # ['Python', 'Java']
print(extract_values('"Python", "Java", "C#"')) # ['Python', 'Java', 'C#']
print(extract_values('"Python" , "Java", "C#"')) # ['Python', 'Java', 'C#']
print(extract_values('"Python", "Java", "C#"')) # ['Python', 'Java', 'C#']
print(extract_values('"Python", "Java", "C#", "Ruby"')) # ['Python', 'Java', 'C#', 'Ruby']
print(extract_values('"Python", "Java", "C#", "Ruby", "Kotlin"')) # ['Python', 'Java', 'C#', 'Ruby', 'Kotlin']
print(extract_values('"Python", "Java", "C#", "Ruby", "Kotlin", "Scala"')) # ['Python', 'Java', 'C#', 'Ruby', 'Kotlin', 'Scala']
print(extract_values('"Python", "Java", "C#", "Ruby", "Kotlin", "Scala", "Swift"')) # ['Python', 'Java', 'C#', 'Ruby', 'Kotlin', 'Scala', 'Swift']
print(extract_values('"Python", "Java", "C#", "Ruby", "Kotlin", "Scala", "Swift", "JavaScript"')) # ['Python', 'Java', 'C#', 'Ruby', 'Kotlin', 'Scala', 'Swift', 'JavaScript']
print(extract_values('"Python", "Java", "C#", "Ruby", "Kotlin", "Scala", "Swift", "JavaScript", "TypeScript"')) # ['Python', 'Java', 'C#', 'Ruby', 'Kotlin', 'Scala', 'Swift', 'JavaScript', 'TypeScript']
print(extract_values('"Python", "Java", "C#", "Ruby", "Kotlin", "Scala", "Swift", "JavaScript", "TypeScript", "Go"')) # ['Python', 'Java', 'C#', 'Ruby', 'Kotlin', 'Scala', 'Swift', 'JavaScript', 'TypeScript', 'Go']
print(extract_values('"Python", "Java", "C#", "Ruby", "Kotlin", "Scala", "Swift", "JavaScript", "TypeScript", "Go", "C++"')) # ['Python', 'Java', 'C#', 'Ruby', 'Kotlin', 'Scala', 'Swift', 'JavaScript', 'TypeScript', 'Go', 'C++']
print(extract_values('"Python", "Java", "C#", "Ruby", "Kotlin", "Scala", "Swift", "JavaScript", "TypeScript", "Go", "C++", "Perl"')) # ['Python', 'Java', 'C#', 'Ruby', 'Kotlin', 'Scala', 'Swift', 'JavaScript', 'TypeScript', 'Go', 'C++', 'Perl']
print(extract_values('"Python", "Java", "C#", "Ruby", "Kotlin", "Scala", "Swift", "JavaScript", "TypeScript", "Go", "C++", "Perl", "Lua"')) # ['Python', 'Java', 'C#', 'Ruby', 'Kotlin', 'Scala', 'Swift', 'JavaScript', 'TypeScript', 'Go', 'C++', 'Perl', 'Lua