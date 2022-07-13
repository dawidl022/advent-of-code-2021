from util.run import run
from part1 import count_increasing


def solution(data: list[int]) -> int:
    windows = [data[i] + data[i + 1] + data[i + 2]
               for i in range(len(data) - 2)]
    return count_increasing(windows)


if __name__ == "__main__":
    run(solution)
