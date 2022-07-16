from collections import Counter
from itertools import chain
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    @property
    def points_on_line(self) -> list[Point]:
        if self.p1.x == self.p2.x:
            start_y = min(self.p1.y, self.p2.y)
            end_y = max(self.p1.y, self.p2.y)

            return [Point(self.p1.x, y) for y in range(start_y, end_y + 1)]
        elif self.p1.y == self.p2.y:
            start_x = min(self.p1.x, self.p2.x)
            end_x = max(self.p1.x, self.p2.x)

            return [Point(x, self.p1.y) for x in range(start_x, end_x + 1)]
        return []


def count_points(lines: list[Line]) -> Counter[Point]:
    return Counter(chain.from_iterable([line.points_on_line for line in lines]))


def count_overlapping_points(point_counts: dict[Point, int]) -> int:
    return len([p for p, count in point_counts.items() if count >= 2])


def solution(lines: list[Line]) -> int:
    point_counts = count_points(lines)
    return count_overlapping_points(point_counts)
