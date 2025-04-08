import re
from collections import defaultdict
from dataclasses import dataclass
from typing import Generator


def read_input_file(file_name: str) -> dict:
    # Lazily read the file and yield particles
    particles = {}
    with open(file_name) as f:
        for i, line in enumerate(f):
            p = tuple(map(int, re.findall(r'(-?\d+)', line)))
            particles[i] = Point(p[0:3], p[3:6], p[6:])
    return particles


@dataclass(frozen=True)
class Point:
    p: tuple[int, int, int]
    v: tuple[int, int, int]
    a: tuple[int, int, int]

    def update(self) -> 'Point':
        # Update velocity and position based on acceleration
        new_v = (
            self.v[0] + self.a[0],
            self.v[1] + self.a[1],
            self.v[2] + self.a[2],
        )
        new_p = (
            self.p[0] + new_v[0],
            self.p[1] + new_v[1],
            self.p[2] + new_v[2],
        )
        return Point(new_p, new_v, self.a)


def manhattan_distance(p: Point, i: int = 0) -> int:
    if i == 0:
        # Position distance
        return abs(p.p[0]) + abs(p.p[1]) + abs(p.p[2])
    elif i == 1:
        # Velocity distance
        return abs(p.v[0]) + abs(p.v[1]) + abs(p.v[2])
    elif i == 2:
        # Acceleration distance
        return abs(p.a[0]) + abs(p.a[1]) + abs(p.a[2])


def remove_collisions(particles: dict) -> dict:
    # Use defaultdict to track particle counts by position
    position_count = defaultdict(list)
    for key, particle in particles.items():
        position_count[particle.p].append(key)

    # Retain only particles that do not collide
    return {
        key: particles[key]
        for pos, keys in position_count.items() if len(keys) == 1
        for key in keys
    }


def compute_part_one(file_name: str) -> str:
    particles = read_input_file(file_name)

    # Find particle with smallest acceleration magnitude
    min_key = min(
        particles.keys(),
        key=lambda k: manhattan_distance(particles[k], 2)
    )
    return f'{min_key=}'


def compute_part_two(file_name: str) -> str:
    particles = read_input_file(file_name)

    # Simulate particle updates and remove collisions
    for _ in range(100):
        # Update all particles
        particles = {key: particle.update() for key, particle in particles.items()}
        # Remove collisions
        particles = remove_collisions(particles)

    return f'{len(particles)=}'


if __name__ == '__main__':
    file_path = 'input/input20.txt'
    print(f"Part I: {compute_part_one(file_path)}")
    print(f"Part II: {compute_part_two(file_path)}")
