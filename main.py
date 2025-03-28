import re
from collections import defaultdict, deque


def read_input_file(file_name: str) -> defaultdict[int, list[int]]:
    connections = defaultdict(list)
    with open(file_name) as f:
        for line in f:
            node, neighbors = line.split('<->')
            connections[int(node)] = list(map(int, re.findall(r'\d+', neighbors)))
    return connections


def get_connected_graph(connections: dict[int, list[int]], start: int) -> set[int]:
    queue = deque([start])
    visited = set()

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(n for n in connections[node] if n not in visited)
    return visited


def compute_part_one(file_name: str) -> str:
    connections = read_input_file(file_name)
    return f"{len(get_connected_graph(connections, 0))}"


def compute_part_two(file_name: str) -> str:
    connections = read_input_file(file_name)
    all_visited = set()
    num_graphs = 0

    for node in connections:
        print(node)
        if node not in all_visited:
            # Find the connected graph for the current node
            graph = get_connected_graph(connections, node)
            print(graph)
            # Update the set of visited nodes
            all_visited.update(graph)
            # Increment the count of distinct graphs
            num_graphs += 1

    return f"{num_graphs}"



if __name__ == "__main__":
    file_path = "input/input12.txt"
    print(f"Part I: {compute_part_one(file_path)}")
    print(f"Part II: {compute_part_two(file_path)}")
