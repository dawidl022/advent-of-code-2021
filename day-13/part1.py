from logic.logic import Point, Line
from util.run import run


def solution(transparency: set[Point], fold_lines: list[Line]) -> int:
    transparency = fold_lines[0].fold(transparency)
    return len(transparency)


if __name__ == "__main__":
    run(solution)
