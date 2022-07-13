from util.run import run
from util.direction.direction import Direction, InvalidDirection


def solution(moves: list[tuple[Direction, int]]):
    aim = 0
    depth = 0
    horizontal = 0

    for (dir, scalar) in moves:
        if dir == Direction.DOWN:
            aim += scalar
        elif dir == Direction.UP:
            aim -= scalar
        elif dir == Direction.FORWARD:
            horizontal += scalar
            depth += aim * scalar
        else:
            raise InvalidDirection()

    return horizontal * depth


if __name__ == "__main__":
    run(solution)
