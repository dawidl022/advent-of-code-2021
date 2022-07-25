from collections import Counter
from typing import Callable


STEPS = 10

char = int  # typealias


def solution(template: list[char], mapping: dict[tuple[char, char], char]) -> int:
    polymer = template
    for _ in range(STEPS):
        new_mers = [mapping[(polymer[i], polymer[i + 1])]
                    for i in range(len(polymer) - 1)]
        polymer = [(polymer if i % 2 == 0 else new_mers)[i // 2]
                   for i in range(2 * len(polymer) - 1)]

    counts = Counter(polymer)
    sorted_counts = counts.most_common(len(counts))

    return sorted_counts[0][1] - sorted_counts[-1][1]


def run(solution: Callable[[list[char], dict[tuple[char, char], char]], int]):
    polymer: list[char] = [ord(x) for x in input()]
    input()  # skip blank line

    mapping: dict[tuple[char, char], char] = {}
    try:
        while True:
            raw_input = input().split(" -> ")
            l, r = (ord(x) for x in raw_input[0])
            mapping[(l, r)] = ord(raw_input[1])
    except EOFError:
        pass

    print(solution(polymer, mapping))


if __name__ == "__main__":
    run(solution)
