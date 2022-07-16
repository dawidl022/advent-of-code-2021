from logic.logic import Point


def print_point_diagram(point_counts: dict[Point, int]):
    for i in range(max([point.y for point in point_counts]) + 1):
        for j in range(max([point.x for point in point_counts]) + 1):
            print(point_counts.get(Point(j, i), "."), end="")
        print()
