from typing import Callable, Type
from logic.logic import Line, Point


def run(line_class: Type[Line], solution: Callable[[list[Line]], int]):
    lines: list[Line] = []

    try:
        while True:
            raw = input()
            raw_points = raw.split(" -> ")
            points = [Point(*[int(x) for x in p.split(",")])
                      for p in raw_points]
            lines.append(line_class(*points))
    except EOFError:
        pass

    print(solution(lines))
