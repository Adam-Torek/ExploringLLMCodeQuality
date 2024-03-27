"""
Write a function to extract values between quotation marks from a string.
assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
"""
def extract_values(input_string):
    """
    Extracts values between quotation marks from a given string.

    :param input_string: string
    :return: list
    """
    values = []
    index = 0
    while index < len(input_string):
        if input_string[index] == '"':
            start_index = index
            index += 1
            while index < len(input_string) and input_string[index] != '"':
                index += 1
            value = input_string[start_index+1:index]
            values.append(value)
            index += 1
        else:
            index += 1
    return values

# Testing the function
assert extract_values('"Python", "PHP", "Java"') == ['Python', 'PHP', 'Java']
assert extract_values('"Python", "PHP, Java"') == ['Python', 'PHP', 'Java']
assert extract_values('"Python"') == ['Python']
assert extract_values('') == []
assert extract_values('"Python" "Java"') == ['Python', 'Java']
assert extract_values('"Python" "Java" "C++"') == ['Python', 'Java', 'C++']
assert extract_values('"Python" "Java" "C++" "Ruby"') == ['Python', 'Java', 'C++', 'Ruby']
assert extract_values('"Python" "Java" "C++" "Ruby" "Go"') == ['Python', 'Java', 'C++', 'Ruby', 'Go']
assert extract_values('"Python" "Java" "C++" "Ruby" "Go" "Swift"') == ['Python', 'Java', 'C++', 'Ruby', 'Go', 'Swift']
assert extract_values('"Python" "Java" "C++" "Ruby" "Go" "Swift" "Rust"') == ['Python', 'Java', 'C++', 'Ruby', 'Go', 'Swift', 'Rust']
assert extract_values('"Python" "Java" "C++" "Ruby" "Go" "Swift" "Rust" "Dart"') == ['Python', 'Java', 'C++', 'Ruby', 'Go', 'Swift', 'Rust', 'Dart']
assert extract_values('"Python" "Java" "C++" "Ruby" "Go" "Swift" "Rust" "Dart" "Kotlin"') == ['Python', 'Java', 'C++', 'Ruby', 'Go', 'Swift', 'Rust', 'Dart', 'Kotlin']
assert extract_values('"Python" "Java" "C++" "Ruby" "Go" "Swift" "Rust" "Dart" "Kotlin" "R"') == ['Python', 'Java', 'C++', 'Ruby', 'Go', 'Swift', 'Rust', 'Dart', 'Kotlin', 'R']
assert extract_values('"Python" "Java" "C++" "Ruby" "Go" "Swift" "Rust" "Dart" "Kotlin" "R" "Scala"') == ['Python', 'Java', 'C++', 'Ruby', 'Go', 'Swift', 'Rust', 'Dart', 'Kotlin', 'R', 'Scala']
assert extract_values('"Python" "Java" "C++" "Ruby" "Go" "Swift" "Rust" "Dart" "Kotlin" "R" "Scala" "JavaScript"') == ['Python', 'Java', 'C++', 'Ruby', 'Go', 'Swift', 'Rust', 'Dart', 'Kotlin', 'R', 'Scala', 'JavaScript']
assert extract_values('"Python" "Java" "C++" "Ruby" "Go" "Swift" "Rust" "Dart" "