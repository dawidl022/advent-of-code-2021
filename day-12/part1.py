from logic.logic import create_solution, END
from util.run import run


def count_paths(curr_vertex: str, vertices: dict[str, set[str]],
                visited: frozenset[str] = frozenset(),
                path: tuple[str, ...] = tuple()) -> int:
    path += (curr_vertex, )

    if curr_vertex == END:
        print(path)  # print entire path taken from start to end
        return 1
    if curr_vertex in visited:
        return 0

    path_count = 0
    visited |= {curr_vertex} if curr_vertex.islower() else set()

    for vertex in vertices[curr_vertex]:
        path_count += count_paths(vertex, vertices, visited, path)

    return path_count


if __name__ == "__main__":
    run(create_solution(count_paths))
