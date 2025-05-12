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
    left_cars = [0] * (n + 1)
    right_cars = [0] * (n + 1)

    for i in range(1, n + 1):
        left_car_position = i + left_cars[i - 1]
        right_car_position = i + right_cars[i - 1]
        if left_car_position == right_car_position:
            return 1
        if left_car_position < right_car_position:
            left_cars[i] = left_car_position
        else:
            right_cars[i] = right_car_position

    return 0


if __name__ == "__main__":
    n = int(input())
    print(car_race_collision(n))