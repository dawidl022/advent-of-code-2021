from typing import Callable


def run(solution: Callable[[list[int]], int]):
    data = [int(x) for x in input().split(",")]
    print(solution(data))
