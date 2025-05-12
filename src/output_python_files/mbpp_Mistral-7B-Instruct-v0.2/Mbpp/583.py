"""
Write a function which returns nth catalan number.
assert catalan_number(10)==16796
"""
def catalan_number(n):
    if n < 0:
        raise ValueError("n must be non-negative integer")
    if n == 0:
        return 1
    return (4*(8*n-1)//(2*n+1)) * catalan_number(n-1)

if __name__ == "__main__":
    import sys
    try:
        n = int(sys.argv[1])
        print(catalan_number(n))
    except (IndexError, ValueError):
        print("Usage: python catalan.py <non-negative-integer>")