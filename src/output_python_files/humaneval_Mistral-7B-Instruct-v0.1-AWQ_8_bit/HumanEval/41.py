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
    left_cars = []
    right_cars = []
    num_collisions = 0

    # Add cars to left and right sides
    for i in range(n):
        left_cars.append(i)
        right_cars.append(i)

    # Loop through left and right cars
    while left_cars and right_cars:
        # Find the index of the leftmost car and the rightmost car
        left_index = left_cars[0]
        right_index = right_cars[-1]

        # Check if the leftmost car is greater than the rightmost car
        if left_index > right_index:
            # If so, remove the leftmost car from the left side
            left_cars.pop(0)
            num_collisions += 1
        else:
            # If not, remove the rightmost car from the right side
            right_cars.pop(-1)
            num_collisions += 1

    # Return the number of collisions
    return num_collisions