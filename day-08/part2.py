from dis import dis
from typing import Callable, NamedTuple


class DigitInput(NamedTuple):
    digit_def: list[str]
    summable: list[str]


class LogicError(Exception):
    pass


def solution(digit_inputs: list[DigitInput]) -> int:
    result = 0
    for inp in digit_inputs:
        display = ["" for _ in range(10)]
        buckets = partition_by_length(inp.digit_def)
        display[1] = buckets[2][0]

        for five in buckets[5]:
            if display[1][0] in five and display[1][1] in five:
                display[3] = five
                break

        compliment_of_3 = set("abcdefg") - set(display[3])

        for six in buckets[6]:
            if len(compliment_of_3 & set(six)) == 2 and len(set(display[1]) & set(six)) == 2:
                display[0] = six
            elif len(set(display[1]) & set(six)) == 1:
                display[6] = six

        for six in buckets[6]:
            if len(set(display[1]) & set(six)) == 2 and six != display[0]:
                display[9] = six
                break

        lo = (set(display[1]) & set(display[6]) & set(display[9])).pop()
        hi = (set(display[1]) - set(lo)).pop()
        phi = (set(display[6]) - set(display[9])).pop()

        for digit in buckets[5]:
            if hi in digit and lo in digit:
                if phi in digit:
                    display[0] = digit
                else:
                    display[3] = digit
            elif hi in digit:
                display[2] = digit
            elif lo in digit:
                display[5] = digit
            else:
                raise LogicError()

        display[4] = buckets[4][0]
        display[7] = buckets[3][0]
        display[8] = buckets[7][0]

        power = 1000
        for summable in inp.summable:
            for val, digit in enumerate(display):
                if set(summable) == set(digit):
                    result += val * power
            power //= 10

    return result


def partition_by_length(l: list[str]) -> dict[int, list[str]]:
    parts: dict[int, list[str]] = {}
    for item in l:
        parts[len(item)] = parts.get(len(item), []) + [item]
    return parts


def run(solution: Callable[[list[DigitInput]], int]):
    data = []
    try:
        while True:
            l, r = input().split(" | ")
            data.append(DigitInput(l.split(), r.split()))
    except EOFError:
        pass

    print(solution(data))


if __name__ == "__main__":
    run(solution)
