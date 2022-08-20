from curses import raw
from typing import Callable
from util.pixel import Pixel


def run(solution: Callable[[list[list[Pixel]], list[Pixel]], int]):
    algorithm = Pixel.fromList(input())
    input()  # skip blank line

    raw_matrix = []

    try:
        while True:
            raw_matrix.append(input())
    except EOFError:
        pass

    source_map = Pixel.fromMatrix(raw_matrix)
    print(solution(source_map, algorithm))
