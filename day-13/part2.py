from typing import Iterable
from logic.logic import Point, Line
from util.run import run


def solution(transparency: set[Point], fold_lines: list[Line]):
    for line in fold_lines:
        transparency = line.fold(transparency)

    print_points(transparency)


def print_points(points: Iterable[Point]):
    max_point = max(points)
    for i in range(max_point.y + 1):
        for j in range(max_point.x + 1):
            if Point(j, i) in points:
                print("#", end="")
            else:
                print(".", end="")
        print()


if __name__ == "__main__":
    run(solution)
