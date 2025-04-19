import datetime
import re
from collections import deque
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


def compute_part_one(file_name: str) -> str:
    components = read_input_file(file_name)
    queue = deque()
    for component in components:
        if not is_start_component(component):
            continue
        other_components = components.copy()
        other_components.remove(component)
        if component[0] == 0:
            queue.append(([component], [c for c in other_components if not is_start_component(c)]))
        else:
            queue.append(([flip(component)], [c for c in other_components if not is_start_component(c)]))
    max_strength = 0

    plt.ion()
    fig, ax = plt.subplots()
    x, y = [], []
    line, = ax.plot(x, y)
    plt.xlabel('Length')
    plt.ylabel('Delay (s)')

    longest_bridge_found = datetime.datetime.now()
    longest_bridge = 0
    while queue:
        bridge, components = queue.popleft()
        if len(bridge) > longest_bridge:
            longest_bridge = len(bridge)
            delay = (datetime.datetime.now() - longest_bridge_found).total_seconds()
            longest_bridge_found = datetime.datetime.now()
            x.append(longest_bridge)
            y.append(delay)
            line.set_data(x, y)
            ax.relim()
            ax.autoscale_view()
            plt.draw()
            plt.pause(0.1)

        extended_bridge = False
        for component in components:
            fit = is_fit(bridge[-1], component)
            if fit != 0:
                extended_bridge = True
                other_components = components.copy()
                other_components.remove(component)
                new_bridge=bridge.copy()
                if fit == 1:
                    new_bridge.append(component)
                if fit == -1:
                    new_bridge.append(flip(component))
                queue.append((new_bridge, other_components))

        if not extended_bridge:
            strength = calculate_bridge_strength(bridge)
            if strength > max_strength:
                max_strength = strength

    print(f"Runtime: {sum(y)}s")

    return f"{max_strength= }"


def compute_part_two(file_name: str) -> str:
    content = read_input_file(file_name)
    return "part 2 not yet implemented"


if __name__ == '__main__':
    file_path = 'input/input24.txt'
    print(f"Part I: {compute_part_one(file_path)}")
    print(f"Part II: {compute_part_two(file_path)}")

    plt.ioff()
    plt.show()