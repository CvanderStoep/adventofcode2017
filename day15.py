from tqdm import tqdm

def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()
    content = list(map(int, content))


    return content

def calculate_next_value(generator: int, factor: int) -> int:
    generator = generator * factor % 2147483647

    return generator

def compare_lowest_bit(number1: int, number2: int):
    # print(f'{number1: 032b}')
    # print(f'{number2: 032b}')

    return number1 & (2**16 -1) ==number2 & (2**16 -1)


def compute_part_one() -> str:
    generatorA, generatorB = 699, 124
    factorA, factorB = 16807, 48271

    total_matches = 0
    for _ in tqdm(range(40_000_000)):
        generatorA = calculate_next_value(generatorA, factorA)
        generatorB = calculate_next_value(generatorB, factorB)
        if compare_lowest_bit(generatorA, generatorB):
            total_matches += 1

    return f'{total_matches= }'


def compute_part_two() -> str:
    generatorA, generatorB = 699, 124
    factorA, factorB = 16807, 48271

    total_matches = 0
    for _ in tqdm(range(5_000_000)):
        while True:
            generatorA = calculate_next_value(generatorA, factorA)
            if generatorA % 4 == 0:
                break

        while True:
            generatorB = calculate_next_value(generatorB, factorB)
            if generatorB % 8 == 0:
                break

        if compare_lowest_bit(generatorA, generatorB):
            total_matches += 1

    return f'{total_matches= }'


if __name__ == '__main__':
    file_path = 'input/input0.txt'
    print(f"Part I: {compute_part_one()}")
    print(f"Part II: {compute_part_two()}")