from collections import defaultdict


def read_input_file(file_name: str) -> list:
    try:
        with open(file_name) as f:
            content = f.read().splitlines()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return []
    except IOError:
        print(f"Error: Could not read the file '{file_name}'.")
        return []


def process_instruction(registers: dict, instruction: str, max_value: int) -> tuple[dict, int]:
    register1, modify, digit1, _, register2, operator, digit2 = instruction.split()
    register_value = registers[register2]
    condition_met = eval(str(register_value) + operator + digit2)
    if condition_met:
        if modify == 'inc':
            registers[register1] += int(digit1)
        else:
            registers[register1] -= int(digit1)

    max_value = max(max_value, max(registers.values()) )
    return registers, max_value

def compute_part(file_name: str) -> None:
    registers = defaultdict(int)

    instructions = read_input_file(file_name)
    max_value = 0
    for instruction in instructions:
        registers, max_value = process_instruction(registers, instruction, max_value)

    max_register_value = max(registers.values())

    print(f'partI: The maximum value of the register after all operations is: {max_register_value}')
    print(f'partII: The maximum value during the operations: {max_value}')



if __name__ == '__main__':
    file_path = 'input/input8.txt'
    compute_part(file_path)
