"""
Write a function to sort a dictionary by value.
assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
"""

def sort_counter(d):
    return sorted(d.items(), key=lambda x: x[1], reverse=True)


def test_sort_counter():
    assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
    assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87, 'Biology':90})==[('Chemistry', 87), ('Physics', 83), ('Math', 81), ('Biology', 90)]
    assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87, 'Biology':90, 'History':95})==[('Chemistry', 87), ('Physics', 83), ('Math', 81), ('Biology', 90), ('History', 95)]
    assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87, 'Biology':90, 'History':95, 'Geography':98})==[('Chemistry', 87), ('Physics', 83), ('Math', 81), ('Biology', 90), ('History', 95), ('Geography', 98)]
    assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87, 'Biology':90, 'History':95, 'Geography':98, 'Psychology':99})==[('Chemistry', 87), ('Physics', 83), ('Math', 81), ('Biology', 90), ('History', 95), ('Geography', 98), ('Psychology', 99)]
    assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87, 'Biology':90, 'History':95, 'Geography':98, 'Psychology':99, 'Music':100})==[('Chemistry', 87), ('Physics', 83), ('Math', 81), ('Biology', 90), ('History', 95), ('Geography', 98), ('Psychology', 99), ('Music', 100)]
    assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87, 'Biology':90, 'History':95, 'Geography':98, 'Psychology':99, 'Music':100, 'Science':101})==[('Chemistry', 87), ('Physics', 83), ('Math', 81), ('Biology', 90), ('History', 95), ('Geography', 98), ('Psychology', 99), ('Music', 100), ('Science', 101)]
    assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87, 'Biology':90, 'History':95, 'Geography':98, 'Psychology':99, 'Music':100, 'Science':101, 'Art':102})==[('Chemistry', 87), ('Physics', 83), ('Math', 81), ('Biology', 90), ('History', 95), ('Geography', 98), ('Psychology', 99), ('Music', 100), ('Science', 101), ('Art', 102)]
    assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87, 'Biology':90, 'History':95, 'Geography':98, 'Psychology':