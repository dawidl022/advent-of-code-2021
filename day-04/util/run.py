from typing import Callable
from .types import Board


def run(solution: Callable[[list[int], list[Board]], int]):
    numbers: list[int] = [int(x) for x in input().split(",")]
    boards: list[Board] = []

    input()  # skip initial blank line
    curr_board: Board = []
    try:
        while True:
            raw = input()
            if len(raw) == 0:
                boards.append(curr_board)
                curr_board = []
                continue

            row = [int(x) for x in raw.split()]
            curr_board.append(row)
    except EOFError:
        pass

    boards.append(curr_board)

    print(solution(numbers, boards))
