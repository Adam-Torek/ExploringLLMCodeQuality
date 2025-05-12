"""
Write a function to convert more than one list to nested dictionary.
assert convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92])==[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
"""
def convert_list_dictionary(list_ids, list_names, list_scores):
    """
    :param list_ids: list of ids
    :param list_names: list of names
    :param list_scores: list of scores
    :return: list of dictionaries where each dictionary has id as key and name and score as nested key value pairs
    """
    result = []
    for i in range(len(list_ids)):
        nested_dict = {}
        nested_dict[list_ids[i]] = {}
        nested_dict[list_ids[i]][list_names[i]] = list_scores[i]
        result.append(nested_dict)
    return result

# Testing the function
assert convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92])==[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]