from logic.logic import create_solution, START, END
from util.run import run


def count_paths(curr_vertex: str, vertices: dict[str, set[str]],
                visited: frozenset[str] = frozenset(),
                repeated: str = "") -> int:

    if curr_vertex == END:
        return 1
    if curr_vertex in visited:
        if curr_vertex not in (START, END) and repeated == "":
            repeated = curr_vertex
        else:
            return 0

    path_count = 0
    visited |= {curr_vertex} if curr_vertex.islower() else set()

    for vertex in vertices[curr_vertex]:
        path_count += count_paths(vertex, vertices, visited, repeated)

    return path_count


if __name__ == "__main__":
    run(create_solution(count_paths))
