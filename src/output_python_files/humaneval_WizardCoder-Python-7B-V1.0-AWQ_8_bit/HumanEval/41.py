def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """
    return n * (n - 1) // 2


# Example usage:
print(car_race_collision(5))  # Output: 10
print(car_race_collision(10))  # Output: 45
print(car_race_collision(100))  # Output: 4950

# Note: The output is the same as the formula n * (n-1) // 2, which is the number of
# unique pairs of cars that can collide.  The // operator is integer division.

# The function can be optimized by using a formula that doesn't involve loops or recursion.
# However, the current implementation is simple and easy to understand.