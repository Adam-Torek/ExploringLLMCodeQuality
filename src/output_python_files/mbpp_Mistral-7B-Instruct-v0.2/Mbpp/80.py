"""
Write a function to find the nth tetrahedral number.
assert tetrahedral_number(5) == 35
"""
def tetrahedral_number(n):
    """
    Calculate the nth tetrahedral number
    """
    return (n*(n+1))//2

if __name__ == "__main__":
    n = 5
    assert tetrahedral_number(n) == 35
    print(f"The {n}th tetrahedral number is {tetrahedral_number(n)}")