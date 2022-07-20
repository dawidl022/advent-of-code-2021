from logic.logic import are_surroundings_taller
from util.run import run


def solution(heightmap: list[list[int]]) -> int:
    total = 0

    for i in range(len(heightmap)):
        for j in range(len(heightmap[i])):
            if are_surroundings_taller(heightmap, i, j):
                total += 1 + heightmap[i][j]

    return total


if __name__ == "__main__":
    run(solution)
