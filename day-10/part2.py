from collections import deque
from util.mapping import OPENING
from util.run import run

POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def solution(chunks_lines: list[str]) -> int:
    scores: list[int] = []

    for line in chunks_lines:
        stack: deque[str] = deque()
        for char in line:
            if char in OPENING:
                stack.append(char)
            else:
                expected = OPENING[stack.pop()]
                if char != expected:
                    break
        else:
            scores.append(calc_score(stack))

    return sorted(scores)[len(scores) // 2]


def calc_score(stack: deque[str]) -> int:
    score = 0
    while len(stack) > 0:
        expected = OPENING[stack.pop()]
        score *= 5
        score += POINTS[expected]

    return score


if __name__ == "__main__":
    run(solution)
