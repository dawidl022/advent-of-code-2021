from __future__ import annotations
from typing import Callable


def solution(range_x: range, range_y: range) -> int:
    met: set[tuple[int, int]] = set()

    for i in range(max(range_x) + 1):
        found_x, stopped_at_x = find_step_to_x_pos_mappings(range_x, i)
        if len(found_x) == 0:
            continue

        met |= find_max_y_given_x(range_y, i, found_x, stopped_at_x)

    return len(met)


def find_step_to_x_pos_mappings(range_x: range, x_velocity: int) -> tuple[dict[int, int], int]:
    found_x: dict[int, int] = {}
    pos_x = 0

    for i in range(x_velocity, 0, -1):
        pos_x += i
        if pos_x in range_x:
            found_x[x_velocity - i] = pos_x

    return found_x, pos_x


def find_max_y_given_x(range_y: range, x_velocity: int, x_step_mapping: dict[int, int], stopped_at_x: int) -> set[tuple[int, int]]:
    met: set[tuple[int, int]] = set()
    search_up = True
    search_down = True
    j = 0
    while search_up or search_down:
        search_for = get_searchable_velocities(j, search_up, search_down)

        for v in search_for:
            try:
                reached = is_target_reached_given_x_and_y(
                    range_y, v, x_step_mapping, stopped_at_x)
            except GoneTooFarUp:
                search_up = False
            except GoneTooFarDown:
                search_down = False
            else:
                if reached:
                    met.add((x_velocity, v))
        j += 1

    return met


def get_searchable_velocities(base_velocity: int, search_up: bool, search_down: bool) -> list[int]:
    velocities = []

    if search_up:
        velocities.append(base_velocity)
    if search_down:
        velocities.append(-base_velocity)

    return velocities


def is_target_reached_given_x_and_y(range_y: range, y_velocity: int, x_step_mapping: dict[int, int], stopped_at_x: int) -> bool:
    step_count = 0
    pos_y = 0
    target_reached = False

    if pos_y + y_velocity < min(range_y):
        raise GoneTooFarDown()

    while step_count <= max(x_step_mapping) or (stopped_at_x in x_step_mapping.values() and pos_y >= min(range_y)):
        pos_y += y_velocity
        y_velocity -= 1

        if pos_y == 0 and y_velocity < min(range_y):
            raise GoneTooFarUp()

        if (step_count in x_step_mapping or stopped_at_x in x_step_mapping.values() and step_count > max(x_step_mapping)) and pos_y in range_y:
            target_reached = True

        step_count += 1

    if pos_y > max(range_y):
        raise GoneTooFarUp()

    return target_reached


class GoneTooFarUp(Exception):
    pass


class GoneTooFarDown(Exception):
    pass


def run(solution: Callable[[range, range], int]):
    _, _, raw_x, raw_y = input().split()
    x_min, x_max = (int(x) for x in raw_x.strip("x=,").split(".."))
    y_min, y_max = (int(y) for y in raw_y.strip("y=").split(".."))

    range_x = range(x_min, x_max + 1)
    range_y = range(y_min, y_max + 1)

    print(solution(range_x, range_y))


if __name__ == "__main__":
    run(solution)
