from util.run import run
from util.types import Board
from logic.logic import mark_number_if_present, has_winning_row, sum_of_unmarked_numbers


def solution(numbers: list[int], boards: list[Board]) -> int:
    for number in numbers:
        for board in boards:
            mark_number_if_present(number, board)

            if has_winning_row(board):
                return number * sum_of_unmarked_numbers(board)

    raise NoWinningBoardException()


class NoWinningBoardException(Exception):
    pass


if __name__ == "__main__":
    run(solution)
