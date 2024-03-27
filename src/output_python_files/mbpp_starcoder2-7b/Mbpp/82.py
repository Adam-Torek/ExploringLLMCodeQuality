"""
Write a function to find the volume of a sphere.
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
"""

def volume_sphere(radius):
    return (4/3) * math.pi * (radius**3)

assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
<file_sep>/01_python_basics/02_strings/02_string_methods.py
"""
String methods
"""

# capitalize
print("hello".capitalize())

# casefold
print("Hello".casefold())

# center
print("hello".center(20, "*"))

# count
print("hello".count("l"))

# encode
print("hello".encode())

# endswith
print("hello".endswith("o"))

# expandtabs
print("hello\thello".expandtabs())

# find
print("hello".find("l"))

# format
print("hello".format())

# index
print("hello".index("l"))

# isalnum
print("hello".isalnum())

# isalpha
print("hello".isalpha())

# isdecimal
print("123".isdecimal())

# isdigit
print("123".isdigit())

# isidentifier
print("hello".isidentifier())

# islower
print("hello".islower())

# isnumeric
print("123".isnumeric())

# isprintable
print("hello".isprintable())

# isspace
print(" ".isspace())

# istitle
print("Hello".istitle())

# isupper
print("HELLO".isupper())

# join
print(" ".join(["hello", "world"]))

# ljust
print("hello".ljust(20, "*"))

# lower
print("HELLO".lower())

# lstrip
print("   hello".lstrip())

# maketrans
print("hello".maketrans("el", "ip"))

# partition
print("hello".partition("l"))

# replace
print("hello".replace("l", "p"))

# rfind
print("hello".rfind("l"))

# rindex
print("hello".rindex("l"))

# rjust
print("hello".rjust(20, "*"))

# rpartition
print("hello".rpartition("l"))

# rsplit
print("hello".rsplit("l"))

# rstrip
print("   hello".rstrip())

# split
print("hello".split("l"))

# splitlines
print("hello\nworld".splitlines())

# startswith
print("hello".startswith("h"))

# strip
print("   hello   ".strip())

# swapcase
print("Hello".swapcase())

# title
print("hello".title())

# translate
print("hello".translate("el"))

# upper
print("hello".upper())

# zfill
print("hello".zfill(20))
<file_sep>/01_python_basics/01_numbers/01_numbers.py
"""
Numbers
"""

# addition
print(1 + 1)

# subtraction
print(1 - 1)

# multiplication
print(1 * 1)

# division
print(1 / 1)

# floor division
print(1 // 1)

# modulo
print(1 % 1)

# exponentiation
print(1 ** 1)

# absolute value
print(abs(-1))

# round
print(round(1.23456789, 2))

# type conversion
print(int(1.23456789))
print(float(1))
<file_sep>/01_python_basics/02_strings/01_strings.py
"""
Strings
"""

# string
print("hello")

# string with single quotes
print('hello')

# string with double quotes
print("hello")

# string with triple quotes
print("""hello""")

# string with triple single quotes
print('''hello''')