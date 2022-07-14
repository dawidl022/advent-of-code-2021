from typing import Callable


def run(solution: Callable[[list[int], int], int]):
    data = []
    try:
        while True:
            raw = input()
            digit_count = len(raw)
            data.append(int(raw, 2))
    except EOFError:
        pass

    print(solution(data, digit_count))
