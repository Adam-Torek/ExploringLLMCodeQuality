"""
Write a function that takes in a dictionary and integer n and filters the dictionary to only include entries with values greater than or equal to n.
assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
"""


def dict_filter(d, n):
    return {k: v for k, v in d.items() if v >= n}


print(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 170))
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}

print(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 165))
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165}

print(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 190))
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}

print(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 180))
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165}

print(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 175))
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165}

print(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 160))
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165}

print(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 150))
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165}

print(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 140))
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165}

print(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 130))
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165}

print(dict_filter({'Cierra Vega': 175, 'Ald