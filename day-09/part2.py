import math
from logic.logic import are_surroundings_taller, MAX_HEIGHT
from util.run import run


def solution(heightmap: list[list[int]]) -> int:
    basin_sizes: list[int] = []

    for i in range(len(heightmap)):
        for j in range(len(heightmap[i])):
            if are_surroundings_taller(heightmap, i, j):
                basin_sizes.append(size_of_basin(heightmap, i, j, set()))

    return math.prod(sorted(basin_sizes, reverse=True)[:3])


def size_of_basin(heightmap: list[list[int]], i: int, j: int, visited: set[tuple[int, int]]) -> int:
    if is_out_of_bounds(heightmap, i, j) or (i, j) in visited or heightmap[i][j] == MAX_HEIGHT:
        return 0

    visited.add((i, j))
    return 1 + \
        size_of_basin(heightmap, i - 1, j, visited) + \
        size_of_basin(heightmap, i + 1, j, visited) + \
        size_of_basin(heightmap, i, j - 1, visited) + \
        size_of_basin(heightmap, i, j + 1, visited)


def is_out_of_bounds(heightmap: list[list[int]], i: int, j: int) -> bool:
    return i < 0 or i >= len(heightmap) or j < 0 or j >= len(heightmap[i])


if __name__ == "__main__":
    run(solution)
