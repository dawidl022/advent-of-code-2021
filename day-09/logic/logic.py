MAX_HEIGHT = 9


def are_surroundings_taller(heightmap: list[list[int]], i: int, j: int) -> bool:
    left = left_value(heightmap, i, j)
    right = right_value(heightmap, i, j)
    up = up_value(heightmap, i, j)
    down = down_value(heightmap, i, j)

    center = heightmap[i][j]

    return center < left and center < right and center < up and center < down


def left_value(heightmap: list[list[int]], i: int, j: int) -> int:
    return heightmap[i][j - 1] if j > 0 else MAX_HEIGHT


def right_value(heightmap: list[list[int]], i: int, j: int) -> int:
    return heightmap[i][j + 1] if j < len(heightmap[i]) - 1 else MAX_HEIGHT


def up_value(heightmap: list[list[int]], i: int, j: int) -> int:
    return heightmap[i - 1][j] if i > 0 else MAX_HEIGHT


def down_value(heightmap: list[list[int]], i: int, j: int) -> int:
    return heightmap[i + 1][j] if i < len(heightmap) - 1 else MAX_HEIGHT
