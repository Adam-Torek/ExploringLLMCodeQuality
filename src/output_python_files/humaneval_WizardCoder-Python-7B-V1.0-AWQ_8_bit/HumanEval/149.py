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
    lst = [word for word in lst if len(word) % 2 == 0]
    return sorted(lst, key=lambda x: (len(x), x))



def test_list_sort():
    assert list_sort(["aa", "a", "aaa"]) == ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert list_sort(["apple", "banana", "cherry", "grape", "kiwi"]) == ["apple", "grape", "banana", "kiwi"]
    assert list_sort(["apple", "banana", "cherry", "grape", "kiwi", "orange", "strawberry"]) == ["apple", "grape", "banana", "kiwi", "orange", "strawberry"]
    assert list_sort(["apple", "banana", "cherry", "grape", "kiwi", "orange", "strawberry", "kiwi"]) == ["apple", "grape", "banana", "kiwi", "orange", "strawberry"]
    assert list_sort(["apple", "banana", "cherry", "grape", "kiwi", "orange", "strawberry", "kiwi", "kiwi"]) == ["apple", "grape", "banana", "kiwi", "orange", "strawberry"]
    assert list_sort(["apple", "banana", "cherry", "grape", "kiwi", "orange", "strawberry", "kiwi", "kiwi", "kiwi"]) == ["apple", "grape", "banana", "kiwi", "orange", "strawberry"]
    assert list_sort(["apple", "banana", "cherry", "grape", "kiwi", "orange", "strawberry", "kiwi", "kiwi", "kiwi", "kiwi"]) == ["apple", "grape", "banana", "kiwi", "orange", "strawberry"]
    assert list_sort(["apple", "banana", "cherry", "grape", "kiwi", "orange", "strawberry", "kiwi", "kiwi", "kiwi", "kiwi", "kiwi"]) == ["apple", "grape", "banana", "kiwi", "orange", "strawberry"]
    assert list_sort(["apple", "banana", "cherry", "grape", "kiwi", "orange", "strawberry", "kiwi", "kiwi", "kiwi", "kiwi", "kiwi", "kiwi"]) == ["apple", "grape", "banana", "kiwi", "orange", "strawberry"]
    assert list_sort(["apple", "banana", "cherry", "grape", "kiwi", "orange", "strawberry", "kiwi", "kiwi", "kiwi", "kiwi", "kiwi", "kiwi", "kiwi"] == ["apple", "grape", "banana", "kiwi", "orange", "strawberry"]



if __name__ == "__main__":
    test_list_sort()
    print("All test cases passed")