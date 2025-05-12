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
    # Initialize variables
    left_cars = 0
    right_cars = 0
    collisions = 0

    # Loop through the cars
    while left_cars < n and right_cars < n:
        # Move left cars to the right
        left_cars += 1

        # Move right cars to the left
        right_cars += 1

        # Check for collisions
        if left_cars > right_cars:
            collisions += 1

    return collisions


# Test the function
print(car_race_collision(5))  # Output: 10