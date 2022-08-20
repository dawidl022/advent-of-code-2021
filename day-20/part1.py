import itertools
from util.pixel import Pixel
from util.run import run


class PixelEnhancer:
    def __init__(self, source_map: list[list[Pixel]], algorithm: list[Pixel]) -> None:
        self.map = source_map
        self.algorithm = algorithm
        self.infinite_pixel = Pixel.DARK

    def enhance(self) -> None:
        target_map = [[Pixel.DARK for _ in range(
            len(self.map) + 2)] for _ in range(len(self.map) + 2)]

        for i in range(-1, len(self.map) + 1):
            for j in range(-1, len(self.map[0]) + 1):
                target_map[i + 1][j + 1] = self._enhance_pixel(i, j)

        self.map = target_map

        # if algorithm[0] is a light pixel, alternate between light and
        # dark pixels for the infinite pixels
        self.infinite_pixel = Pixel(
            (self.infinite_pixel.value + self.algorithm[0].value) % 2)

    @property
    def lit_pixel_count(self) -> int:
        return list(itertools.chain.from_iterable(self.map)).count(Pixel.LIGHT)

    def _enhance_pixel(self, i: int, j: int) -> Pixel:
        return self.algorithm[self._get_enhance_index(i, j)]

    def _get_enhance_index(self, target_i: int, target_j: int) -> int:
        index = 0

        for i in range(target_i - 1, target_i + 2):
            for j in range(target_j - 1, target_j + 2):
                index <<= 1
                if self._is_out_of_bounds(i, j):
                    index += self.infinite_pixel.value
                else:
                    index += self.map[i][j].value

        return index

    def _is_out_of_bounds(self, i, j) -> bool:
        return i < 0 or i >= len(self.map) or j < 0 or j >= len(self.map[i])


def solution(source_map: list[list[Pixel]], algorithm: list[Pixel]) -> int:
    enhancer = PixelEnhancer(source_map, algorithm)
    for _ in range(2):
        enhancer.enhance()
    return enhancer.lit_pixel_count


if __name__ == "__main__":
    run(solution)
