def generate_spiral_with_turning(n):
    # Directions: right (0,1), up (-1,0), left (0,-1), down (1,0)
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    direction_index = 0  # Start with moving right

    x, y = 0, 0  # Starting at the center
    visited = {(x, y): 1}  # Track visited coordinates, initializing (0,0)

    for i in range(2, n + 1):
        # Move in the current direction
        dx, dy = directions[direction_index]
        x, y = x + dx, y + dy

        # Determine if a left turn is needed (check the next cell to the left)
        left_index = (direction_index + 1) % 4  # Next direction (turning left)
        left_dx, left_dy = directions[left_index]
        if (x + left_dx, y + left_dy) not in visited:
            direction_index = left_index  # Turn left

        # Mark the current cell as visited
        visited[(x, y)] = i

    return visited

grid = generate_spiral_with_turning(10)
print(grid)

from collections import defaultdict
from itertools import cycle

def generate_spiral_with_itertools(n):
    # Define the directions: right, up, left, down
    directions = cycle([(0, 1), (-1, 0), (0, -1), (1, 0)])

    x, y = 0, 0  # Start at the center
    visited = {(x, y): 1}  # Keep track of visited coordinates
    current_direction = next(directions)  # Start with moving right

    for i in range(2, n + 1):
        # Move in the current direction
        dx, dy = current_direction
        x, y = x + dx, y + dy

        # Check if a left turn is needed
        # Peek at the next direction (left turn)
        left_direction = next(directions)
        left_dx, left_dy = left_direction
        if (x + left_dx, y + left_dy) not in visited:
            current_direction = left_direction  # Turn left
        else:
            # Revert the cycle to stay on the same direction
            current_direction = dx, dy  # Remain in the same direction

        # Mark the current cell as visited
        visited[(x, y)] = i

    return visited

grid = generate_spiral_with_itertools(10)
print(grid)