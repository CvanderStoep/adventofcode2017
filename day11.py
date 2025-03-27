def read_input_file(file_name: str) -> list[str]:
    with open(file_name) as f:
        content = f.read().splitlines()
    content = content[0].split(',')

    return content

def process_route(direction: str, position: tuple) -> tuple:
    directions = {'n': (0, 2), 's': (0, -2), 'ne': (2, 1), 'se': (2, -1), 'nw': (-2, 1), 'sw': (-2, -1)}
    dx, dy = directions[direction]
    x, y = position
    position = x + dx, y + dy
    return position

def calculated_distance(position: tuple) -> int:
    x, y = position
    distance = (abs(y) + abs(x) // 2) // 2

    return distance

def compute_part(file_name: str) -> str | None:
    route = read_input_file(file_name)
    print(route)
    start = (0, 0)
    visited_locations = set()

    for step in route:
        start = process_route(step, start)
        visited_locations.add(start)
    print(f'end of route: {start}')
    print(f'part I: {calculated_distance(start)= } ')

    max_steps = 0
    for pos in visited_locations:
        max_steps = max(max_steps, calculated_distance(pos))
    print(f'part II: {max_steps= }')



if __name__ == '__main__':
    file_path = 'input/input11.txt'
    compute_part(file_path)