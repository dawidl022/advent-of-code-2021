from logic.logic import increment_energy_levels, MAX_ENERGY
from util.run import run


def solution(octos: list[list[int]]) -> int:
    octo_count = len(octos) * len(octos[0])
    step = 0

    while True:
        step += 1
        increment_energy_levels(octos)

        flashing_octos = 0
        for i in range(len(octos)):
            for j in range(len(octos)):
                if octos[i][j] > MAX_ENERGY:
                    flashing_octos += 1
                    octos[i][j] = 0

        if flashing_octos == octo_count:
            return step


if __name__ == "__main__":
    run(solution)
