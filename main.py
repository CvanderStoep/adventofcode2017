def get_weight(programs: list, program: str) -> int:
    weight = 0
    for line in programs:
        if line.startswith(program):
            # Get the weight of the current program
            weight = int(re.findall(r'(\d+)', line)[0])

            # If the program has no children, return its weight
            if '->' not in line:
                return weight
            else:
                # Extract the children and their weights
                children = re.findall(r'[a-z]+', line)[1:]
                child_weights = [get_weight(programs, child) for child in children]

                # Check if the children's weights are balanced
                if len(set(child_weights)) != 1:
                    # Find the correct and incorrect weights
                    weight_counts = {w: child_weights.count(w) for w in child_weights}
                    correct_weight = [w for w in weight_counts if weight_counts[w] > 1][0]
                    incorrect_weight = [w for w in weight_counts if weight_counts[w] == 1][0]

                    # Find the unbalanced child
                    unbalanced_child = children[child_weights.index(incorrect_weight)]

                    # Compute the corrected weight for the unbalanced child
                    unbalanced_child_line = [l for l in programs if l.startswith(unbalanced_child)][0]
                    unbalanced_child_current_weight = int(re.findall(r'(\d+)', unbalanced_child_line)[0])
                    corrected_weight = unbalanced_child_current_weight + (correct_weight - incorrect_weight)

                    return f"Corrected weight: {corrected_weight}"

                # Sum the weights of the program and its children
                weight += sum(child_weights)
    return weight
