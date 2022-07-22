from logic.logic import increment_energy_levels, MAX_ENERGY
from util.run import run


STEPS = 100


def solution(octos: list[list[int]]) -> int:
    flash_count = 0

    for _ in range(STEPS):
        increment_energy_levels(octos)

        for i in range(len(octos)):
            for j in range(len(octos)):
                if octos[i][j] > MAX_ENERGY:
                    flash_count += 1
                    octos[i][j] = 0

    return flash_count


if __name__ == "__main__":
    run(solution)
