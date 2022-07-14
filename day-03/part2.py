from util.run import run
from collections import namedtuple

Partitions = namedtuple("Partitions", ["zeroes", "ones"])


def partition_based_on_bit(number: list[int], masking_bit: int) -> Partitions:
    zeros = [x for x in number if x & masking_bit == 0]
    ones = [x for x in number if x & masking_bit != 0]

    return Partitions(zeros, ones)


def longer_list_or_right(a: list, b: list) -> list:
    return a if len(a) > len(b) else b


def shorter_list_or_left(a: list, b: list) -> list:
    return a if len(a) <= len(b) else b


class MaskUnderflowException(Exception):
    pass


def solution(numbers: list[int], bin_digit_count: int) -> int:
    mask = 0b1 << (bin_digit_count - 1)
    oxygen_rating_candidates = numbers
    o2_scrubber_candidates = numbers

    while len(oxygen_rating_candidates) > 1 or len(o2_scrubber_candidates) > 1:
        if mask < 0b1:
            raise MaskUnderflowException()

        if len(oxygen_rating_candidates) > 1:
            zeros, ones = partition_based_on_bit(
                oxygen_rating_candidates, mask)
            oxygen_rating_candidates = longer_list_or_right(
                zeros, ones)

        if len(o2_scrubber_candidates) > 1:
            zeros, ones = partition_based_on_bit(
                o2_scrubber_candidates, mask)
            o2_scrubber_candidates = shorter_list_or_left(
                zeros, ones)

        mask >>= 1

    return oxygen_rating_candidates[0] * o2_scrubber_candidates[0]


if __name__ == "__main__":
    run(solution)
