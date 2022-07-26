from part1 import solution as shortest_path_cost
from util.run import run


def solution(map: list[list[int]]) -> int:
    new_top_map = expand_top_rows(map)
    new_map = expand_columns(new_top_map)

    return shortest_path_cost(new_map)


def expand_top_rows(map):
    new_top_map: list[list[int]] = []
    for i in range(len(map)):
        new_row: list[int] = []
        for n in range(5):
            for j in range(len(map[i])):
                new_digit = map[i][j] + n
                while new_digit > 9:
                    new_digit -= 9
                new_row.append(new_digit)
        new_top_map.append(new_row)
    return new_top_map


def expand_columns(new_top_map):
    new_map: list[list[int]] = []
    for n in range(5):
        for i in range(len(new_top_map)):
            new_row = []
            for j in range(len(new_top_map[i])):
                new_digit = new_top_map[i][j] + n
                while new_digit > 9:
                    new_digit -= 9
                new_row.append(new_digit)
            new_map.append(new_row)
    return new_map


if __name__ == "__main__":
    run(solution)
