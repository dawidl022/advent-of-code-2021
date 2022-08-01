from __future__ import annotations
from collections import deque
from enum import Enum, auto
from functools import partial
from math import prod
from typing import Callable, NamedTuple


class State(Enum):
    VERSION = (auto(), 3)
    TYPE_ID = (auto(), 3)
    LENGTH_ID = (auto(), 1)
    LENGTH = (auto(), 15)
    SUB_PACKET_COUNT = (auto(), 11)
    GROUP = (auto(), 5)

    def __new__(cls, value: int, *args, **kwargs):
        """Boilerplate to initialise custom enum"""
        state = object.__new__(cls)
        state._value_ = value
        return state

    def __init__(self, _: int, bits: int):
        self.bits = bits


class Operation(Enum):
    SUM = sum
    PROD = prod
    MIN = min
    MAX = max
    # partials are used to avoid pitfall described at: https://stackoverflow.com/a/68771326/
    IDENTITY = partial(lambda x: x)
    GREATER_THAN = partial(lambda a: 1 if a[0] > a[1] else 0)
    LESS_THAN = partial(lambda a: 1 if a[0] < a[1] else 0)
    EQUAL = partial(lambda a: 1 if a[0] == a[1] else 0)


operations = (
    Operation.SUM,
    Operation.PROD,
    Operation.MIN,
    Operation.MAX,
    Operation.IDENTITY,
    Operation.GREATER_THAN,
    Operation.LESS_THAN,
    Operation.EQUAL,
)


class ParseResult(NamedTuple):
    values: list[int]
    bit_index: int
    bits_read: int
    packets_read: int


def parse_packet(transmission: int, bit_index: int, bit_count: int, packet_count: int) -> ParseResult:
    members: deque[int | Operation] = deque()
    state: State = State.VERSION
    value_buffer = 0
    bits_read = 0
    packets_read = 0

    while (bits_read < bit_count or packets_read < packet_count) and bit_index >= state.bits - 1:
        read = read_bits(transmission, bit_index, state)
        # print_action(state, read)
        bit_index -= state.bits
        bits_read += state.bits

        # finite-state machine like dispatch
        if state == State.VERSION:
            state = State.TYPE_ID

        elif state == State.TYPE_ID:
            if read == 4:
                state = State.GROUP
            else:
                members.append(operations[read])
                state = State.LENGTH_ID

        elif state == State.GROUP:
            value_buffer <<= 4
            value_buffer += read & 0b1111
            if (read & 0b10000) == 0:
                state = State.VERSION
                members.append(value_buffer)
                value_buffer = 0
                packets_read += 1

        elif state == State.LENGTH_ID:
            if read == 0:
                state = State.LENGTH
            else:
                state = State.SUB_PACKET_COUNT

        else:
            if state == State.LENGTH:
                res = parse_packet(transmission, bit_index, read, 0)

            elif state == State.SUB_PACKET_COUNT:
                res = parse_packet(transmission, bit_index, 0, read)

            else:
                raise InvalidStateError()

            op = members.pop()
            assert isinstance(op, Operation)
            members.append(op.value(res.values))

            bit_index = res.bit_index
            bits_read += res.bits_read
            packets_read += 1
            state = State.VERSION

    values = []
    while len(members) > 0:
        val = members.popleft()
        assert isinstance(val, int)
        values.append(val)

    return ParseResult(values, bit_index, bits_read, packets_read)


class InvalidStateError(Exception):
    pass


def solution(transmission: int, bit_count: int) -> int:
    return parse_packet(transmission, bit_count - 1, bit_count, 0).values[0]


def print_action(state, read):
    print(state)
    print(read, bin(read))
    print()


def read_bits(transmission: int, bit_index: int, state: State):
    mask = gen_mask(bit_index, state.bits)
    return (transmission & mask) >> (bit_index - state.bits + 1)


def gen_mask(bit_index: int, mask_length: int):
    mask = 0
    for i in range(mask_length):
        mask += 1 << bit_index - i
    return mask


def run(solution: Callable[[int, int], int]):
    raw_input = input()
    print(solution(int(raw_input, 16), len(raw_input) * 4))


if __name__ == "__main__":
    run(solution)
