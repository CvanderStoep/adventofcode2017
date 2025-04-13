def grid_to_dict(input_grid):
    grid_dict = {}
    for row_index, row in enumerate(input_grid.splitlines()):
        for col_index, char in enumerate(row):
            grid_dict[(row_index, col_index)] = char
    return grid_dict

# Example usage
input_grid = """..#
#..
..."""

grid_dict = grid_to_dict(input_grid)
print(grid_dict)
