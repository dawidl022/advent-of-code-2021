from typing import Callable


MAGIC_LENGTHS = frozenset([2, 3, 4, 7])


def solution(output_digits: list[str]) -> int:
    count = 0
    for digit in output_digits:
        if len(digit) in MAGIC_LENGTHS:
            count += 1

    return count


def run(solution: Callable[[list[str]], int]):
    data = []
    try:
        while True:
            data += input().split(" | ")[1].split()
    except EOFError:
        pass

    print(solution(data))


if __name__ == "__main__":
    run(solution)
