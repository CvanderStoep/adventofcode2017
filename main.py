import itertools

def digits(string: str):
    return [int(n) for n in string.split()]

with open('input/input2.txt') as fp:
    rows = [digits(line) for line in fp.read().strip().splitlines()]

print(sum(b-a for a, *_, b in map(sorted, rows)))
print(sum(b//a for row in rows for a, b in itertools.combinations(sorted(row), 2) if b%a==0))