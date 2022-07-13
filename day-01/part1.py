from util.run import run


def solution(data: list[int]) -> int:
    return count_increasing(data)


def count_increasing(data: list[int]) -> int:
    count = 0
    for i in range(len(data) - 1):
        if data[i + 1] > data[i]:
            count += 1
    return count


if __name__ == "__main__":
    run(solution)
