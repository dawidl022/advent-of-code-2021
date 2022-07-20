from typing import Callable


def run(solution: Callable[[list[list[int]]], int]):
    data: list[list[int]] = []
    try:
        while True:
            data.append([int(x) for x in input()])
    except EOFError:
        pass

    print(solution(data))
