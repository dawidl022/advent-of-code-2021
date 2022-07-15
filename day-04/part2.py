from util.run import run
from util.types import Board
from logic.logic import mark_number_if_present, has_winning_row, sum_of_unmarked_numbers


def solution(numbers: list[int], boards: list[Board]) -> int:
    won_boards_indices = set()

    for number in numbers:
        for i in range(len(boards)):
            if i in won_boards_indices:
                continue

            board = boards[i]
            mark_number_if_present(number, board)

            if has_winning_row(board):
                won_boards_indices.add(i)

            if len(won_boards_indices) == len(boards):
                return number * sum_of_unmarked_numbers(board)

    raise NotAllBoardsWonException()


class NotAllBoardsWonException(Exception):
    pass


if __name__ == "__main__":
    run(solution)
