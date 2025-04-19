import datetime
import re
from collections import deque


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content

def is_fit(c1: str, c2:str) -> bool:
    p11, p12 = c1.split('/')
    p21, p22 = c2.split('/')
    p11, p12, p21, p22 = int(p11), int(p12), int(p21), int(p22)
    if p11==0 and p21==0:
        return False
    if p11 ==0 and p22==0:
        return False
    if p12 ==0 and p21 ==0:
        return False
    if p12 ==0 and p22 ==0:
        return False
    if p11==p21 or p11==p22 or p12==p21 or p12==p22:
        return True

    return False

def calculate_bridge_strength(bridge:list) -> int:
    bridge_strength = 0
    for component in bridge:
        p1, p2 = component.split('/')
        p1, p2 = int(p1), int(p2)
        bridge_strength += p1
        bridge_strength += p2
    return bridge_strength

def compute_part_one(file_name: str) -> str:
    components = read_input_file(file_name)
    # print(components)
    queue = deque()
    bridge = []
    for component in components:
        ports = list(map(int, re.findall(r'(\d+)', component)))
        # print(ports)
        if 0 in ports:
            other_components = components.copy()
            other_components.remove(component)
            queue.append(([component],other_components))
    max_strength = 0
    best_bridge = None
    longest_bridge_found = datetime.datetime.now()
    longest_bridge = 0
    while queue:
        bridge, components = queue.popleft()
        if len(bridge) > longest_bridge:
            longest_bridge = len(bridge)
            delay = datetime.datetime.now() - longest_bridge_found
            longest_bridge_found = datetime.datetime.now()
            print(f'{longest_bridge = } -- {delay.total_seconds():.2f}s')
        strength = calculate_bridge_strength(bridge)
        if strength > max_strength:
            max_strength = strength
            best_bridge = bridge

        for component in components:
            if is_fit(bridge[-1], component):
                other_components = components.copy()
                other_components.remove(component)
                new_bridge=bridge.copy()
                new_bridge.append(component)
                queue.append((new_bridge, other_components))

    print(best_bridge, max_strength)


    return "part 1 not yet implemented"


def compute_part_two(file_name: str) -> str:
    content = read_input_file(file_name)
    print(content)
    return "part 2 not yet implemented"


if __name__ == '__main__':
    file_path = 'input/input24.txt'
    print(f"Part I: {compute_part_one(file_path)}")
    print(f"Part II: {compute_part_two(file_path)}")