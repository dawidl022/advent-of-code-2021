from util.run import run
from util.direction.direction import Direction, InvalidDirection


def solution(moves: list[tuple[Direction, int]]) -> int:
    horizontal = 0
    depth = 0

    for (dir, scalar) in moves:
        if dir == Direction.FORWARD:
            horizontal += scalar
        elif dir == Direction.DOWN:
            depth += scalar
        elif dir == Direction.UP:
            depth -= scalar
        else:
            raise InvalidDirection()

    return horizontal * depth


if __name__ == "__main__":
    run(solution)
