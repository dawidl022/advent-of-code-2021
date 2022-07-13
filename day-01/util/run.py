from typing import Callable


def run(solution: Callable[[list[int]], int]):
    data = []
    try:
        while True:
            data.append(int(input()))
    except EOFError:
        pass

    print(solution(data))
