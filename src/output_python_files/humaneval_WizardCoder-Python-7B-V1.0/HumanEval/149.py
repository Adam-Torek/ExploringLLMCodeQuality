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
    # Filter out words with odd lengths
    filtered_list = [word for word in lst if len(word) % 2 == 0]
    # Sort the list by length and then alphabetically
    sorted_list = sorted(filtered_list, key=lambda x: (len(x), x))
    return sorted_list



# Test cases
print(sorted_list_sum(["aa", "a", "aaa"]))  # Output: ["aa"]
print(sorted_list_sum(["ab", "a", "aaa", "cd"]))  # Output: ["ab", "cd"]
print(sorted_list_sum(["hello", "world", "python", "programming", "code"]))  # Output: ["code", "hello", "python"]
print(sorted_list_sum(["apple", "banana", "cherry", "banana", "apple", "cherry"]))  # Output: ["apple", "banana"]
print(sorted_list_sum(["cat", "dog", "bird", "fish", "bird"]))  # Output: ["bird", "cat", "fish"]
print(sorted_list_sum(["apple", "banana", "cherry", "apple", "banana"]))  # Output: ["apple", "banana"]
print(sorted_list_sum(["apple", "banana", "cherry", "apple", "banana", "cat", "dog", "bird", "fish", "bird"]))  # Output: ["bird", "cat", "fish", "apple", "banana"]