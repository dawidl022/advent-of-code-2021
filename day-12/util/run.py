
from typing import Callable


def run(solution: Callable[[list[tuple[str, str]]], int]):
    edges: list[tuple[str, str]] = []
    try:
        while True:
            l, r = input().split("-")
            edges.append((l, r))
    except EOFError:
        pass

    print(solution(edges))
