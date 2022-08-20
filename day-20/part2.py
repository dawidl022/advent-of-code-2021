from util.pixel import Pixel
from util.run import run
from logic.enhancer import PixelEnhancer


def solution(source_map: list[list[Pixel]], algorithm: list[Pixel]) -> int:
    enhancer = PixelEnhancer(source_map, algorithm)
    for _ in range(50):
        enhancer.enhance()
    return enhancer.lit_pixel_count


if __name__ == "__main__":
    run(solution)
