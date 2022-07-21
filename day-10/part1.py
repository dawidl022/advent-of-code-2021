from collections import deque
from util.mapping import OPENING
from util.run import run

POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def solution(chunks_lines: list[str]) -> int:
    points = 0

    for line in chunks_lines:
        stack: deque[str] = deque()
        for char in line:
            if char in OPENING:
                stack.append(char)
            else:
                expected = OPENING[stack.pop()]
                if char != expected:
                    points += POINTS[char]
                    break

    return points


if __name__ == "__main__":
    run(solution)
