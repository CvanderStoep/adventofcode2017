from collections import deque


def read_input_file(file_name: str) -> list[str]:
    with open(file_name) as f:
        return f.read().strip().split(',')


def move(position: tuple, direction: str) -> tuple:
    directions = {'n': (0, 2), 's': (0, -2), 'ne': (2, 1), 'se': (2, -1), 'nw': (-2, 1), 'sw': (-2, -1)}
    dx, dy = directions[direction]
    x, y = position
    return x + dx, y + dy


def compute_steps(file_name: str, part: int) -> str:
    route = read_input_file(file_name)
    directions = {'n': (0, 2), 's': (0, -2), 'ne': (2, 1), 'se': (2, -1), 'nw': (-2, 1), 'sw': (-2, -1)}
    visited, start, max_distance = set(), (0, 0), 0

    # Traverse the route to calculate visited locations
    for step in route:
        start = move(start, step)
        max_distance = max(max_distance, sum(abs(coord) for coord in start) // 2)
        visited.add(start)

    # Breadth-First Search
    queue, visited_nodes = deque([(0, (0, 0))]), set()
    while queue:
        steps, position = queue.popleft()
        if position in visited_nodes:
            continue
        visited_nodes.add(position)
        if part == 1 and position == start:
            return f'{steps= }'
        if part == 2 and position in visited:
            visited.remove(position)
            if not visited:
                return f'{max_distance= }'
        for dx, dy in directions.values():
            queue.append((steps + 1, (position[0] + dx, position[1] + dy)))


if __name__ == '__main__':
    file_path = 'input/input11.txt'
    print(f"Part I: {compute_steps(file_path, part=1)}")
    print(f"Part II: {compute_steps(file_path, part=2)}")
