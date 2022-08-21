from typing import Callable


def run(solution: Callable[[int, int], int]):
    p1_start = int(input().split()[-1])
    p2_start = int(input().split()[-1])

    print(solution(p1_start, p2_start))
