import datetime
import re
from collections import deque, defaultdict
import matplotlib.pyplot as plt


def read_component(component: str) -> (int, int):
    ports = list(map(int, re.findall(r'(\d+)', component)))
    return ports[0], ports[1]


def read_input_file(file_name: str) -> list[(int, int)]:
    with open(file_name) as f:
        return list(map(read_component, f.read().splitlines()))


def is_fit(c1: (int, int), c2: (int, int)) -> int:
    if c1[1]==c2[0]:
        return 1
    if c1[1]==c2[1]:
        return -1
    return 0


def calculate_bridge_strength(bridge: list[(int, int)]) -> int:
    return sum(sum(component) for component in bridge)


def flip(component: (int, int)) -> (int, int):
    return component[1], component[0]


def is_start_component(component: (int, int)) -> bool:
    return component[0] == 0 or component[1] == 0


def compute_port_map(components: list[(int, int)]) -> dict[(int, int), list[(int, int)]]:
    port_map = defaultdict(list)

    for component in components:
        port_map[component[0]].append((component, 1))
        port_map[component[1]].append((component, -1))

    return port_map


def compute_part_one(file_name: str) -> str:
    components = read_input_file(file_name)

    port_map = compute_port_map(components)

    visited_bridges = set()

    queue = deque()
    for component in components:
        if not is_start_component(component):
            continue
        other_components = components.copy()
        other_components.remove(component)
        start_component = component if component[0] == 0 else flip(component)
        queue.append(([start_component], set([c for c in other_components if not is_start_component(c)])))
    max_strength = 0

    longest_bridge_lengths, delays = [], []

    longest_bridge_found = datetime.datetime.now()
    longest_bridge = 0
    while queue:
        bridge, components = queue.popleft()
        last_port = bridge[-1][1]

        visisted_bridge = (last_port, frozenset(components))
        if visisted_bridge in visited_bridges:
            continue
        visited_bridges.add(visisted_bridge)

        if len(bridge) > longest_bridge:
            longest_bridge = len(bridge)
            delay = (datetime.datetime.now() - longest_bridge_found).total_seconds()
            longest_bridge_found = datetime.datetime.now()
            longest_bridge_lengths.append(longest_bridge)
            delays.append(delay)

        extended_bridge = False

        last_bridge_component = bridge[-1]
        potential_fits = port_map[last_bridge_component[1]]

        for component, orientation in potential_fits:
            if component in components:
                extended_bridge = True
                other_components = components - {component}
                new_bridge=bridge.copy()
                if orientation == 1:
                    new_bridge.append(component)
                if orientation == -1:
                    new_bridge.append(flip(component))
                queue.append((new_bridge, other_components))

        if not extended_bridge:
            strength = calculate_bridge_strength(bridge)
            if strength > max_strength:
                max_strength = strength

    print(f"Runtime: {sum(delays)}s")


    plt.plot(longest_bridge_lengths, delays)
    plt.xlabel('Length')
    plt.ylabel('Delay (s)')
    plt.show()

    return f"{max_strength= }"


def compute_part_two(file_name: str) -> str:
    content = read_input_file(file_name)
    return "part 2 not yet implemented"


if __name__ == '__main__':
    file_path = 'input/input24.txt'
    print(f"Part I: {compute_part_one(file_path)}")
    print(f"Part II: {compute_part_two(file_path)}")
