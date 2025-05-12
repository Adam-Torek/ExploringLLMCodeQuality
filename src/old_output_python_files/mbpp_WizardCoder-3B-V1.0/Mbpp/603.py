"""
Write a function to get all lucid numbers smaller than or equal to a given integer.
assert get_ludic(10) == [1, 2, 3, 5, 7]
"""

def get_ludic(n):
    ludic = []
    for i in range(1, n+1):
        if i % 2 == 0:
            ludic.append(i)
    return ludic

print(get_ludic(10))<|endoftext|>