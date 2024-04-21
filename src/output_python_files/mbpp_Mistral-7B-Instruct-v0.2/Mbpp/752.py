"""
Write a function to find the nth jacobsthal number. https://www.geeksforgeeks.org/jacobsthal-and-jacobsthal-lucas-numbers/ 0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, ...
assert jacobsthal_num(5) == 11
"""

def jacobsthal_num(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (2 * jacobsthal_num(n // 2) + jacobsthal_num(n // 4)) % 2**(n.bit_length())

if __name__ == "__main__":
    for n in [0, 1, 5, 10, 15, 20]:
        print(f"jacobsthal_num({n}) = {jacobsthal_num(n)}")</s>