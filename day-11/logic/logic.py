MAX_ENERGY = 9


def increment_energy_levels(octos):
    for i in range(len(octos)):
        for j in range(len(octos[i])):
            energise_octo(octos, i, j)


def energise_octo(octos: list[list[int]], i: int, j: int):
    if out_of_bounds(octos, i, j):
        return

    octos[i][j] += 1
    if octos[i][j] == MAX_ENERGY + 1:
        energise_surrounding(octos, i, j)


def out_of_bounds(octos, i, j):
    return i < 0 or i >= len(octos) or j < 0 or j >= len(octos[i])


def energise_surrounding(octos: list[list[int]], i: int, j: int):
    energise_octo(octos, i - 1, j - 1)
    energise_octo(octos, i - 1, j)
    energise_octo(octos, i - 1, j + 1)
    energise_octo(octos, i, j - 1)
    energise_octo(octos, i, j + 1)
    energise_octo(octos, i + 1, j - 1)
    energise_octo(octos, i + 1, j)
    energise_octo(octos, i + 1, j + 1)
