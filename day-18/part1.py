from __future__ import annotations
from dataclasses import dataclass
from functools import reduce
import math
from typing import Callable


@dataclass
class Node:
    left: Node | None
    right: Node | None
    value: int | None = None
    parent: Node | None = None

    def __post_init__(self):
        if self.left is not None:
            self.left.parent = self

        if self.right is not None:
            self.right.parent = self

    @staticmethod
    def valued(value: int, parent: Node) -> Node:
        return Node(None, None, value, parent)

    @staticmethod
    def from_list(list: list | int) -> Node:
        if isinstance(list, int):
            return Node(None, None, list, None)

        return Node(Node.from_list(list[0]), Node.from_list(list[1]))

    def as_list(self) -> list | int:
        if self.value is not None:
            return self.value

        assert self.left is not None and self.right is not None
        return [self.left.as_list(), self.right.as_list()]

    def bubble_left(self, sender: Node, value: int):
        if self.parent is None and sender is self.left:
            return

        if sender is self or sender is self.left:
            assert(self.parent is not None)
            return self.parent.bubble_left(self, value)

        assert isinstance(self.left, Node)
        self.left.add_right(value)

    def bubble_right(self, sender: Node, value: int):
        if self.parent is None and sender is self.right:
            return

        if sender is self or sender is self.right:
            assert(self.parent is not None)
            return self.parent.bubble_right(self, value)

        assert isinstance(self.right, Node)
        self.right.add_left(value)

    def add_left(self, value: int):
        if self.value is None:
            assert isinstance(self.left, Node)
            return self.left.add_left(value)

        self.value += value
        self.split_if_necessary()

    def add_right(self, value: int):
        if self.value is None:
            assert isinstance(self.right, Node)
            return self.right.add_right(value)

        self.value += value
        self.split_if_necessary()

    def split_if_necessary(self):
        if self.value < 10:
            return

        half = self.value / 2
        self.left = Node.valued(math.floor(half), self)
        self.right = Node.valued(math.ceil(half), self)
        self.value = None

        if self.calc_level() >= 4:
            self.value = 0
            self.bubble_left(self, self.left.value)
            self.bubble_right(self, self.right.value)

            clear_node(self)

    def calc_level(self) -> int:
        level = 0
        current = self

        while current.parent is not None:
            current = current.parent
            level += 1

        return level


def solution(pairs: list[Node]) -> int:
    result = reduce(add_pairs, pairs)
    print(result.as_list())
    return 0


def add_pairs(pair1: Node, pair2: Node) -> Node:
    node = Node(pair1, pair2)
    reduce_pair(node)
    return node


def reduce_pair(pair: Node, level: int = 0) -> None:
    """Reduction performed in place"""

    if pair.value is not None:
        return

    assert isinstance(pair.left, Node) and isinstance(pair.right, Node)
    if level == 4:
        pair.value = 0
        assert isinstance(pair.left.value, int)
        pair.bubble_left(pair, pair.left.value)

        assert isinstance(pair.right.value, int)
        pair.bubble_right(pair, pair.right.value)

        return clear_node(pair)

    reduce_pair(pair.left, level + 1)
    reduce_pair(pair.right, level + 1)


def clear_node(pair: Node):
    pair.left = None
    pair.right = None


def run(solution: Callable[[list[Node]], int]):
    pairs: list[Node] = input_nodes(input)
    print(solution(pairs))


def input_nodes(nextInput: Callable[[], str]) -> list[Node]:
    nodes: list[Node] = []

    try:
        while True:
            nodes.append(Node.from_list(eval(nextInput())))
    except EOFError:
        pass

    return nodes


if __name__ == "__main__":
    run(solution)
