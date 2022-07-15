from util.types import Board

MARK = -1


def mark_number_if_present(number: int, board: Board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == number:
                board[i][j] = MARK


def has_winning_row(board: Board) -> bool:
    for row in board:
        if all(x == MARK for x in row):
            return True

    for j in range(len(board[0])):
        if all(board[i][j] == MARK for i in range(len(board))):
            return True

    return False


def sum_of_unmarked_numbers(board: Board) -> int:
    sum = 0
    for row in board:
        for cell in row:
            if cell != MARK:
                sum += cell

    return sum
