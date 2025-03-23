import operator
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
    # Map operators to their functions
    ops = {
        '==': operator.eq,
        '!=': operator.ne,
        '>': operator.gt,
        '<': operator.lt,
        '>=': operator.ge,
        '<=': operator.le
    }

    register1, modify, digit1, _, register2, operator_symbol, digit2 = instruction.split()
    condition_met = ops[operator_symbol](registers[register2], int(digit2))

    if condition_met:
        if modify == 'inc':
            registers[register1] += int(digit1)
        elif modify == 'dec':
            registers[register1] -= int(digit1)

    max_value = max(max_value, max(registers.values(), default=0))
    return registers, max_value

def compute_part(file_name: str) -> None:
    registers = defaultdict(int)

    instructions = read_input_file(file_name)
    if not instructions:
        return  # Exit if no instructions were read

    max_value = 0
    for instruction in instructions:
        registers, max_value = process_instruction(registers, instruction, max_value)

    max_register_value = max(registers.values(), default=0)

    print(f'Part I: The maximum value of any register after all operations is: {max_register_value}')
    print(f'Part II: The highest value held in any register during operations is: {max_value}')

if __name__ == '__main__':
    file_path = 'input/input8.txt'
    compute_part(file_path)
