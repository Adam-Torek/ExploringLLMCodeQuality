"""
Write a function to convert more than one list to nested dictionary.
assert convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92])==[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
"""
def convert_list_dictionary(list_keys, list_values, list_values_numbers):
    if len(list_keys) != len(list_values) or len(list_keys) != len(list_values_numbers):
        raise ValueError("The length of lists must be equal")

    result = []
    for i in range(len(list_keys)):
        nested_dict = {}
        nested_dict[list_keys[i]] = {}
        nested_dict[list_keys[i]].update({list_values[i]: list_values_numbers[i]})
        result.append(nested_dict)

    return result

# Test the function
assert convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92])==[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]