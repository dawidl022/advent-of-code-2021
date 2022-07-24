from typing import Callable, Optional
from logic.logic import Point, Line, VerticalLine, HorizontalLine


def run(solution: Callable[[set[Point], list[Line]], Optional[int]]):
    points: set[Point] = set()
    lines: list[Line] = []

    try:
        point_input = True
        while True:
            raw_input = input()
            if len(raw_input) == 0:
                point_input = False
            elif point_input:
                x, y = (int(x) for x in raw_input.split(","))
                points.add(Point(x, y))
            else:
                info = raw_input.split()[2]
                axis, value = info.split("=")
                if axis == "x":
                    lines.append(VerticalLine(int(value)))
                elif axis == "y":
                    lines.append(HorizontalLine(int(value)))

                else:
                    raise ParseError()
    except EOFError:
        pass

    result = solution(points, lines)
    if result is not None:
        print(result)


class ParseError(Exception):
    pass
