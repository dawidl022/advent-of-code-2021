from abc import ABC, abstractmethod
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


class Line(ABC):
    def __init__(self, value: int):
        self.value = value

    def fold(self, transparency: set[Point]) -> set[Point]:
        new_transparency: set[Point] = set()

        for point in transparency:
            if self.should_mirror_point(point):
                new_transparency.add(self.symmetric_point(point))
            else:
                new_transparency.add(point)

        return new_transparency

    @abstractmethod
    def should_mirror_point(self, point: Point) -> bool:
        pass

    @abstractmethod
    def symmetric_point(self, point: Point) -> Point:
        pass


class VerticalLine(Line):
    def should_mirror_point(self, point: Point) -> bool:
        return point.x > self.value

    def symmetric_point(self, point: Point) -> Point:
        return Point(2 * self.value - point.x, point.y)


class HorizontalLine(Line):
    def should_mirror_point(self, point: Point) -> bool:
        return point.y > self.value

    def symmetric_point(self, point: Point) -> Point:
        return Point(point.x, 2 * self.value - point.y)
