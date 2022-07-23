from collections import defaultdict
from typing import Callable


START = "start"
END = "end"


def create_solution(counting_strategy: Callable[[str, dict[str, set[str]]], int]
                    ) -> Callable[[list[tuple[str, str]]], int]:
    def solution(edges: list[tuple[str, str]]) -> int:
        vertices = map_vertices(edges)
        return counting_strategy(START, vertices)

    return solution


def map_vertices(edges) -> dict[str, set[str]]:
    vertices: defaultdict[str, set[str]] = defaultdict(set)
    for edge in edges:
        vertices[edge[0]].add(edge[1])
        vertices[edge[1]].add(edge[0])
    return vertices
