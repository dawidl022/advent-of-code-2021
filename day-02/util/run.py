from typing import Callable
from .direction.direction import Direction


def run(solution: Callable[[list[tuple[Direction, int]]], int]):
    data = []
    try:
        while True:
            dir, scalar = input().split()
            data.append((Direction(dir), int(scalar)))
    except EOFError:
        pass

    print(solution(data))
