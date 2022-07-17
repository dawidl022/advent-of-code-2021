from typing import Callable


def run(solution: Callable[[list[int], int], int], simulation_days: int):
    timers = [int(x) for x in input().split(",")]
    print(solution(timers, simulation_days))
