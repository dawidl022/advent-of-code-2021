from math import prod
from typing import NamedTuple
from logic.ranges import combine_ranges


class Range3D(NamedTuple):
    x: range
    y: range
    z: range

    @staticmethod
    def combine(a: 'Range3D', b: 'Range3D') -> 'Range3D':
        return Range3D(*[combine_ranges(a[i], b[i]) for i in range(len(a))])


class Area3D:
    def __init__(self):
        self.on: list[Range3D] = []

    def add_range(self, x: range, y: range, z: range):
        new_area = Range3D(x, y, z)
        for i, a in enumerate(self.on):
            if all(
                    new_area[j][0] in a[j] or new_area[j][-1] in a[j]
                    or (new_area[j][0] < a[j][0] and new_area[j][-1] > a[j][-1])
                    for j in range(3)):
                self.on[i] = Range3D.combine(a, new_area)
                break
        else:
            self.on.append(Range3D(x, y, z))

    def subtract_range(self, x: range, y: range, z: range):
        pass

    @property
    def area(self) -> int:
        return sum(prod(len(dim) for dim in a) for a in self.on)

    def area_within_bounds(self, x: range, y: range, z: range) -> int:
        pass
