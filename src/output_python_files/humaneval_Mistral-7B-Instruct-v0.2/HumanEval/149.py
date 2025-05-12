def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    # Filter the list to keep only the strings with even length
    filtered_lst = list(filter(lambda x: len(x) % 2 == 0, lst))

    # Sort the filtered list first by length, then alphabetically
    sorted_lst = sorted(filtered_lst, key=lambda x: (len(x), x))

    return sorted_lst

# Test the function
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
assert sorted_list_sum(["apple", "banana", "cherry", "date"]) == ["apple", "banana"]
assert sorted_list_sum(["cat", "cat", "dog", "dog"]) == ["cat"]
assert sorted_list_sum(["apple", "banana", "cherry", "date", "apple"]) == ["apple", "apple", "banana", "cherry", "date"]
assert sorted_list_sum(["apple", "banana", "cherry", "date", "apple", "banana"]) == ["apple", "apple", "banana", "banana", "cherry", "date"]
assert sorted_list_sum(["apple", "banana", "cherry", "date", "apple", "banana", "cherry"]) == ["apple", "apple", "banana", "banana", "cherry", "cherry", "date"]
assert sorted_list_sum(["apple", "banana", "cherry", "date", "apple", "banana", "cherry", "apple"]) == ["apple", "apple", "apple", "banana", "banana", "cherry", "cherry", "date"]
assert sorted_list_sum(["apple", "banana", "cherry", "date", "apple", "banana", "cherry", "apple", "banana"]) == ["apple", "apple", "apple", "apple", "banana", "banana", "cherry", "cherry", "date"]
assert sorted_list_sum(["apple", "banana", "cherry", "date", "apple", "banana", "cherry", "apple", "banana", "cherry"]) == ["apple", "apple", "apple", "apple", "apple", "banana", "banana", "cherry", "cherry", "date"]
assert sorted_list_sum(["apple", "banana", "cherry", "date", "apple", "banana", "cherry", "apple", "banana", "cherry", "cherry"]) == ["apple", "apple", "apple", "apple", "apple", "apple", "banana", "banana", "cherry", "cherry", "cherry"]
assert sorted_list_sum(["apple", "banana", "cherry", "date", "apple", "banana", "cherry", "apple", "banana", "cherry", "cherry", "cherry"]) == ["apple", "apple", "apple", "apple", "apple", "apple", "apple", "banana", "banana", "cherry", "cherry", "cherry"]
assert sorted_list_sum(["apple", "banana", "cherry", "date", "apple", "banana", "cherry",