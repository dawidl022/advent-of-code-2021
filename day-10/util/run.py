from typing import Callable


def run(solution: Callable[[list[str]], int]):
    data = []
    try:
        while True:
            data.append(input())
    except EOFError:
        pass

    print(solution(data))
