def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    # Your code here
    a = str(a)
    b = str(b)
    a = a[-1]
    b = b[-1]
    return int(a) * int(b)


# Examples
print(multiply(148, 412))
print(multiply(19, 28))
print(multiply(2020, 1851))
print(multiply(14, -15))

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def print_results(results):
    for result in results:
        print(result)


def test_multiply():
    assert multiply(148, 412) == 16
    assert multiply(19, 28) == 72
    assert multiply(2020, 1851) == 0
    assert multiply(14, -15) == 20


print_results(test_multiply())

# Write your code here.


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def print_results(results):
    for result in results:
        print(result)


def test_multiply():
    assert multiply(148, 412) == 16
    assert multiply(19, 28) == 72
    assert multiply(2020, 1851) == 0
    assert multiply(14, -15) == 20


print_results(test_multiply())

# Write your code here.


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def print_results(results):
    for result in results:
        print(result)


def test_multiply():
    assert multiply(148, 412) == 16
    assert multiply(19, 28) == 72
    assert multiply(2020, 1851) == 0
    assert multiply(14, -15) == 20


print_results(test_multiply())

# Write your code here.


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def print_results(results):
    for result in results:
        print(result)


def test_multiply():
    assert multiply(148, 412) == 16
    assert multiply(19, 28) == 72
    assert multiply(2020, 1851) == 0
    assert multiply(14, -15) == 20


print_results(test_multiply())

# Write your code here.


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def print_results(results):
    for result in results:
        print(result)


def test_multiply():
    assert multiply(148, 412) == 16
    assert multiply(19, 28) == 72
    assert