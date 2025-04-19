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

def calculate_bridge_strength(bridge:list) -> int:
    bridge_strength = 0
    for component in bridge:
        bridge_strength += component[0]
        bridge_strength += component[1]
    return bridge_strength


def flip(component: (int, int)) -> (int, int):
    return component[1], component[0]


def is_start_component(component: (int, int)) -> bool:
    return component[0] == 0 or component[1] == 0


def compute_fits(components: list[(int, int)]) -> dict[(int, int), list[(int, int)]]:
    fits = defaultdict(list)

    def add_potential_fit(c1, c2):
        fit = is_fit(c1, c2)
        if fit == 1:
            fits[c1].append((c2, 1))
        elif fit == -1:
            fits[c1].append((c2, -1))

    for component in components:
        for other_component in components:
            if component == other_component:
                continue
            add_potential_fit(component, other_component)
            add_potential_fit(flip(component), other_component)

    return fits


def compute_part_one(file_name: str) -> str:
    components = read_input_file(file_name)

    fits = compute_fits(components)

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
        potential_fits = fits[last_bridge_component]

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
