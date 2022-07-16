from logic.logic import Line, Point, solution
from util.run import run


class Line45(Line):
    @property
    def points_on_line(self) -> list[Point]:
        points_90 = super().points_on_line

        if len(points_90) > 0:
            return points_90

        point = min(self.p1, self.p2)
        end_point = max(self.p1, self.p2)
        v_increment = 1 if point.y < end_point.y else -1

        diagonals = []
        while point != end_point:
            diagonals.append(point)
            point = Point(point.x + 1, point.y + v_increment)

        diagonals.append(end_point)
        return diagonals


if __name__ == "__main__":
    run(Line45, solution)
