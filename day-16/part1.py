from dataclasses import dataclass
from enum import Enum, auto
from typing import Callable


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


@dataclass
class SubPacketState:
    on: bool = False
    bits_to_read: int = 0
    packets_to_read: int = 0


def solution(transmission: int, bit_count: int) -> int:
    bit_index = bit_count - 1
    state: State = State.VERSION
    sub_packet = SubPacketState()
    version_count = 0

    while bit_index >= state.bits:
        read = read_bits(transmission, bit_index, state)
        # print_action(state, read)
        bit_index -= state.bits

        # finite-state machine like dispatch
        if state == State.VERSION:
            version_count += read
            state = State.TYPE_ID

        elif state == State.TYPE_ID:
            if read == 4:
                state = State.GROUP
            else:
                state = State.LENGTH_ID

        elif state == State.GROUP:
            if (read & 0b10000) == 0:
                state = State.VERSION

        elif state == State.LENGTH_ID:
            if read == 0:
                state = State.LENGTH
            else:
                state = State.SUB_PACKET_COUNT

        elif state == State.LENGTH:
            sub_packet.on = True
            sub_packet.bits_to_read = read
            state = State.VERSION

        elif state == State.SUB_PACKET_COUNT:
            sub_packet.on = True
            sub_packet.packets_to_read = read + 1
            state = State.VERSION

        if sub_packet.on:
            if sub_packet.bits_to_read > 0:
                sub_packet.bits_to_read -= state.bits
            elif State == State.VERSION and sub_packet.packets_to_read > 0:
                sub_packet.packets_to_read -= 1

            if sub_packet.bits_to_read == 0 and sub_packet.packets_to_read == 0:
                sub_packet.on = False

    return version_count


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
