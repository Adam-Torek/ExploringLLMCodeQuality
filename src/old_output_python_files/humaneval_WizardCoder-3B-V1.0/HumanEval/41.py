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

# Example usage:
n = 10
print(car_race_collision(n))  # Output: 0

n = 20
print(car_race_collision(n))  # Output: 10

n = 30
print(car_race_collision(n))  # Output: 20

n = 40
print(car_race_collision(n))  # Output: 30

n = 50
print(car_race_collision(n))  # Output: 40

n = 60
print(car_race_collision(n))  # Output: 50

n = 70
print(car_race_collision(n))  # Output: 60

n = 80
print(car_race_collision(n))  # Output: 70

n = 90
print(car_race_collision(n))  # Output: 80

n = 100
print(car_race_collision(n))  # Output: 90<|endoftext|>