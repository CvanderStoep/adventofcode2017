def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        return list(map(int, f.read().split()))


def distribute_memory(memory: list) -> list:
    max_index = memory.index(max(memory))
    blocks = memory[max_index]
    memory[max_index] = 0

    for i in range(blocks):
        memory[(max_index + 1 + i) % len(memory)] += 1
    return memory


def find_cycles(memory: list, find_loop: bool = False) -> int:
    seen = {}
    cycles = 0

    while tuple(memory) not in seen:
        seen[tuple(memory)] = cycles
        memory = distribute_memory(memory)
        cycles += 1

    return cycles - seen[tuple(memory)] if find_loop else cycles


def compute_part_one(file_name: str) -> str:
    memory = read_input_file(file_name)
    cycles = find_cycles(memory)
    return f'Number of redistribution cycles before configuration is seen again: {cycles}'


def compute_part_two(file_name: str) -> str:
    memory = read_input_file(file_name)
    loop_size = find_cycles(memory, find_loop=True)
    return f'Size of the infinite loop: {loop_size}'


if __name__ == '__main__':
    file_path = 'input/input6.txt'
    print(f"Part I: {compute_part_one(file_path)}")
    print(f"Part II: {compute_part_two(file_path)}")
