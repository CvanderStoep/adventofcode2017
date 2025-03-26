from collections import deque
directions = {'n': (0, 2), 's': (0, -2), 'ne': (2, 1), 'se': (2, -1), 'nw': (-2, 1), 'sw': (-2, -1)}


def read_input_file(file_name: str) -> list[str]:
    with open(file_name) as f:
        content = f.read().splitlines()
    content = content[0].split(',')

    return content

def process_route(direction: str, position: tuple) -> tuple:
    dx, dy = directions[direction]
    x, y = position
    position = x + dx, y + dy
    return position


def compute_part(file_name: str, part: int) -> str | None:
    route = read_input_file(file_name)
    print(route)
    start = (0, 0)
    max_steps = 0
    visited_locations = set()
    for step in route:
        start = process_route(step, start)
        visited_locations.add(start)
    print(f'end of route: {start}')
    finish = start # take the end of the route calculated above
    start = (0,0)
    steps = 0
    queue = deque()
    queue.append((steps, start))
    visited = set()
    while queue:
        steps, position = queue.popleft()
        if position in visited:
            continue
        if part == 1 and position == finish:
            return f'{steps= }'
        if part == 2:
            if position in visited_locations:
                max_steps = max(max_steps, steps)
                visited_locations.remove(position)
            if len(visited_locations) == 0:
                return f'{max_steps= }'
        visited.add(position)
        for direction in directions.values():
            x, y = position
            dx, dy = direction
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited:
                queue.append((steps + 1, (nx, ny)))


if __name__ == '__main__':
    file_path = 'input/input11.txt'
    print(f"Part I: {compute_part(file_path, part=1)}")
    print(f"Part II: {compute_part(file_path, part=2)}")