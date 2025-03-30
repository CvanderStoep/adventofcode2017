from collections import deque
import numpy as np

# Function to read input from a file
def read_input_file(file_name: str) -> str:
    with open(file_name) as f:
        return f.read().strip()

# Function to convert hexadecimal to binary with 4-digit formatting
def hex_to_binary(hex_string: str) -> str:
    return ''.join(f'{int(c, 16):04b}' for c in hex_string)

# Function to reverse a sublist for the knot hash
def knot_hash(lst: list, l: int, pos: int) -> list:
    array_length = len(lst)
    new_array = lst.copy()
    for i in range(l):
        new_array[(pos + i) % array_length] = lst[(pos + l - i - 1) % array_length]
    return new_array

# Function to compute the dense hash and return the knot hash
def calculate_knot_hash(key_string: str) -> str:
    lengths = [ord(x) for x in key_string] + [17, 31, 73, 47, 23]
    lst = list(range(256))
    skip = 0
    pos = 0
    for _ in range(64):
        for l in lengths:
            lst = knot_hash(lst, l, pos)
            pos = (pos + l + skip) % len(lst)
            skip += 1
    # Compute dense hash and convert to hexadecimal
    dense_hash = [np.bitwise_xor.reduce(lst[i:i + 16]) for i in range(0, 256, 16)]
    return ''.join(f'{x:02x}' for x in dense_hash)

# Function to create the binary grid
def create_binary_grid(file_name: str) -> list:
    puzzle_input = read_input_file(file_name)
    return [
        hex_to_binary(calculate_knot_hash(f"{puzzle_input}-{i}"))
        for i in range(128)
    ]

# Function to compute the number of used squares (Part I)
def compute_part_one(file_name: str) -> str:
    grid = create_binary_grid(file_name)
    number_of_squares = sum(row.count('1') for row in grid)
    return f"{number_of_squares}"

# Function to compute the number of regions (Part II)
def compute_part_two(file_name: str) -> str:
    grid = create_binary_grid(file_name)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    all_visited = set()
    number_of_regions = 0

    for y in range(128):
        for x in range(128):
            if (x, y) not in all_visited and grid[y][x] == '1':
                # Use BFS to explore a new region
                queue = deque([(x, y)])
                while queue:
                    cx, cy = queue.popleft()
                    if (cx, cy) not in all_visited:
                        all_visited.add((cx, cy))
                        for dx, dy in directions:
                            nx, ny = cx + dx, cy + dy
                            if 0 <= nx < 128 and 0 <= ny < 128 and grid[ny][nx] == '1' and (nx, ny) not in all_visited:
                                queue.append((nx, ny))
                number_of_regions += 1

    return f"{number_of_regions}"

# Main execution
if __name__ == "__main__":
    file_path = 'input/input14.txt'  # Replace with your input file path
    print(f"Part I: {compute_part_one(file_path)}")
    print(f"Part II: {compute_part_two(file_path)}")
