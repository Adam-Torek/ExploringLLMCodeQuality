"""
Write a function to sort a dictionary by value.
assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
"""


def sort_counter(d):
    return sorted(d.items(), key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    print(sort_counter({'Math': 81, 'Physics': 83, 'Chemistry': 87}))
    print(sort_counter({'Math': 81, 'Physics': 83, 'Chemistry': 87, 'Biology': 87}))
    print(sort_counter({'Math': 81, 'Physics': 83, 'Chemistry': 87, 'Biology': 87, 'History': 87}))
    print(sort_counter({'Math': 81, 'Physics': 83, 'Chemistry': 87, 'Biology': 87, 'History': 87, 'Geography': 87}))
    print(sort_counter({'Math': 81, 'Physics': 83, 'Chemistry': 87, 'Biology': 87, 'History': 87, 'Geography': 87, 'Psychology': 87}))
    print(sort_counter({'Math': 81, 'Physics': 83, 'Chemistry': 87, 'Biology': 87, 'History': 87, 'Geography': 87, 'Psychology': 87, 'Music': 87}))
    print(sort_counter({'Math': 81, 'Physics': 83, 'Chemistry': 87, 'Biology': 87, 'History': 87, 'Geography': 87, 'Psychology': 87, 'Music': 87, 'Art': 87}))
    print(sort_counter({'Math': 81, 'Physics': 83, 'Chemistry': 87, 'Biology': 87, 'History': 87, 'Geography': 87, 'Psychology': 87, 'Music': 87, 'Art': 87, 'Science': 87}))
    print(sort_counter({'Math': 81, 'Physics': 83, 'Chemistry': 87, 'Biology': 87, 'History': 87, 'Geography': 87, 'Psychology': 87, 'Music': 87, 'Art': 87, 'Science': 87, 'English': 87}))
    print(sort_counter({'Math': 81, 'Physics': 83, 'Chemistry': 87, 'Biology': 87, 'History': 87, 'Geography': 87, 'Psychology': 87, 'Music': 87, 'Art': 87, 'Science': 87, 'English': 87, 'Computer': 87}))
    print(sort_counter({'Math': 81, 'Physics': 83, 'Chemistry': 87, 'Biology': 87, 'History': 87, 'Geography': 87, 'Psychology': 87, 'Music': 87, 'Art': 87, 'Science': 87, 'English': 87, 'Computer': 87, 'Economics': 87}))
    print(sort_counter({'Math': 81, 'Physics': 83, 'Chemistry': 87, 'Biology': 87, 'History': 87, 'Geography': 87, 'Psychology': 87, 'Music': 87, 'Art': 87, 'Science': 87, 'English': 87, 'Computer': 87, 'Economics': 87, 'Business': 87}))
    print(sort_counter