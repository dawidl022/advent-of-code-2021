from dis import dis
from typing import Callable, NamedTuple


class DigitInput(NamedTuple):
    digit_def: list[str]
    summable: list[str]


class SevenFragmentDigitIdentifier:
    def __init__(self, digit_def: list[str]) -> None:
        # maps each digit to its segments
        self._display = ["" for _ in range(10)]
        self._buckets = partition_by_length(digit_def)

    def identify(self) -> list[str]:
        self._locate_one()
        self._locate_three()

        self._locate_zero_and_six()

        self._locate_two_and_five()
        self._locate_remaining_magics_digits()

        return self._display

    def _locate_one(self):
        """
        '1' is the only digit with two segments.

        Based on the knowledge which fragments '1' is composed,
        we can derive all the other digit to fragment mappings.

        The two fragments which make up '1' will be referred to as
        'hi' (top fragment) and 'lo' (bottom fragment).
        """
        self._display[1] = self._buckets[2][0]

    def _locate_three(self):
        """
        '3' is the only digit of 5 fragments which contains the fragments of '1'
        """
        for five in self._buckets[5]:
            if self._display[1][0] in five and self._display[1][1] in five:
                self._display[3] = five
                break

    def _locate_zero_and_six(self):
        """
        Based on the fragments of '1' and '3' we can identify:

        '0' is the only digit of 6 segments which contains the fragments of '1' AND
        the fragments not found in '3'.

        '6' does not contain all fragments of '1', but does contain the fragments
        not found in '3'.

        '9' contains the fragments of '1', but does not contain all fragments not
        found in '3'.
        """
        compliment_of_3 = set("abcdefg") - set(self._display[3])

        for six in self._buckets[6]:
            if len(compliment_of_3 & set(six)) == 2 and len(set(self._display[1]) & set(six)) == 2:
                self._display[0] = six
            elif len(set(self._display[1]) & set(six)) == 1:
                self._display[6] = six
            elif len(compliment_of_3 & set(six)) == 1:
                self._display[9] = six

    def _locate_two_and_five(self):
        """
        Based on the fragments of '6' and '9', we can now identify the hi and
        lo fragments, which are also used to identify '2' and '5'.
        """
        lo = (set(self._display[1]) & set(
            self._display[6]) & set(self._display[9])).pop()
        hi = (set(self._display[1]) - set(lo)).pop()

        for digit in self._buckets[5]:
            if digit == self._display[3]:
                continue
            elif hi in digit:
                self._display[2] = digit
            elif lo in digit:
                self._display[5] = digit
            else:
                raise self.LogicError()

    def _locate_remaining_magics_digits(self):
        """
        Locate all digits (except for '1') that have unique fragment lengths
        """
        self._display[4] = self._buckets[4][0]
        self._display[7] = self._buckets[3][0]
        self._display[8] = self._buckets[7][0]

    class LogicError(Exception):
        pass


def solution(digit_inputs: list[DigitInput]) -> int:
    result = 0
    for inp in digit_inputs:
        result += summable_value(inp.summable,
                                 SevenFragmentDigitIdentifier(inp.digit_def).identify())
    return result


def partition_by_length(l: list[str]) -> dict[int, list[str]]:
    parts: dict[int, list[str]] = {}
    for item in l:
        parts[len(item)] = parts.get(len(item), []) + [item]
    return parts


def summable_value(digits_to_sum, display) -> int:
    total = 0
    power = 10 ** (len(digits_to_sum) - 1)
    for summable in digits_to_sum:
        for val, digit in enumerate(display):
            if set(summable) == set(digit):
                total += val * power
        power //= 10

    return total


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
