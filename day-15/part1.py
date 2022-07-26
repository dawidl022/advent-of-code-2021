from __future__ import annotations
from dataclasses import dataclass, field
import math
from queue import PriorityQueue
from util.run import run

# my first implementation of Dijkstra's algorithm


@dataclass(order=True)
class Node:
    coords: tuple[int, int] = field(compare=False)
    cost: float = math.inf


def solution(map: list[list[int]]) -> int:
    nodes_queue: PriorityQueue[Node] = PriorityQueue()
    visited: set[tuple[int, int]] = set()
    target = (len(map) - 1, len(map[0]) - 1)

    nodes_queue.put(Node((0, 0), 0))

    while not nodes_queue.empty() > 0:
        node = nodes_queue.get()
        if node.coords == target:
            break

        if node.coords in visited:
            continue

        enque_neighbours(map, nodes_queue, node)

        visited.add(node.coords)

    return int(node.cost)


def enque_neighbours(map: list[list[int]], nodes_queue: PriorityQueue[Node],
                     node: Node):
    left = Node((node.coords[0], node.coords[1] - 1))
    enque_unless_out_of_bounds(map, nodes_queue, left, node.cost)

    right = Node((node.coords[0], node.coords[1] + 1))
    enque_unless_out_of_bounds(map, nodes_queue, right, node.cost)

    up = Node((node.coords[0] - 1, node.coords[1]))
    enque_unless_out_of_bounds(map, nodes_queue, up, node.cost)

    down = Node((node.coords[0] + 1, node.coords[1]))
    enque_unless_out_of_bounds(map, nodes_queue, down, node.cost)


def enque_unless_out_of_bounds(map: list[list[int]], queue: PriorityQueue[Node],
                               node: Node, cost: float):
    if not out_of_bounds(map, node) and node.coords:
        node.cost = cost + map[node.coords[0]][node.coords[1]]
        queue.put(node)


def out_of_bounds(map: list[list[int]], node: Node):
    return node.coords[0] < 0 or node.coords[0] >= len(map) or \
        node.coords[1] < 0 or node.coords[1] >= len(map[node.coords[0]])


if __name__ == "__main__":
    run(solution)
