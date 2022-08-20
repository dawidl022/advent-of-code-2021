import unittest
from part1 import PixelEnhancer, Pixel


class TestPixel(unittest.TestCase):
    def test_light_from_hash_symbol(self):
        self.assertEqual(Pixel.fromSymbol('#'), Pixel.LIGHT)

    def test_dark_from_dot_symbol(self):
        self.assertEqual(Pixel.fromSymbol('.'), Pixel.DARK)

    def test_exception_from_other_symbols(self):
        with self.assertRaises(ValueError):
            Pixel.fromSymbol('!')

    def test_from_matrix(self):
        self.assertEqual(Pixel.fromMatrix([
            "#..#.",
            "#....",
            "##..#",
            "..#..",
            "..###",
        ]), [
            [Pixel.LIGHT, Pixel.DARK, Pixel.DARK, Pixel.LIGHT, Pixel.DARK],
            [Pixel.LIGHT, Pixel.DARK, Pixel.DARK, Pixel.DARK, Pixel.DARK],
            [Pixel.LIGHT, Pixel.LIGHT, Pixel.DARK, Pixel.DARK, Pixel.LIGHT],
            [Pixel.DARK, Pixel.DARK, Pixel.LIGHT, Pixel.DARK, Pixel.DARK],
            [Pixel.DARK, Pixel.DARK, Pixel.LIGHT, Pixel.LIGHT, Pixel.LIGHT]
        ])


class TestPixelEnhancer(unittest.TestCase):
    def setUp(self):
        source_map = Pixel.fromMatrix([
            "#..#.",
            "#....",
            "##..#",
            "..#..",
            "..###",
        ])
        algorithm = Pixel.fromList("..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#")
        self.enhancer = PixelEnhancer(source_map, algorithm)

    def test_get_enhance_index_middle_pixel(self):
        self.assertEqual(self.enhancer._get_enhance_index(2, 2), 34)

    def test_get_enhance_index_topleft_corner_pixel(self):
        self.assertEqual(self.enhancer._get_enhance_index(0, 0), 18)

    def test_get_enhance_index_bottomright_corner_pixel(self):
        self.assertEqual(self.enhancer._get_enhance_index(4, 4), 48)

    def test_enhance_middle_pixel(self):
        self.assertEqual(self.enhancer._enhance_pixel(2, 2), Pixel.LIGHT)

    def test_enhcane_bottomright_pixel(self):
        self.assertEqual(self.enhancer._enhance_pixel(4, 4), Pixel.DARK)

    def test_enhcance_once(self):
        self.enhancer.enhance()
        self.assertEqual(self.enhancer.map, Pixel.fromMatrix([
            ".##.##.",
            "#..#.#.",
            "##.#..#",
            "####..#",
            ".#..##.",
            "..##..#",
            "...#.#.",
        ]))

    def test_enhance_twice(self):
        for _ in range(2):
            self.enhancer.enhance()

        self.assertEqual(self.enhancer.map, Pixel.fromMatrix([
            ".......#.",
            ".#..#.#..",
            "#.#...###",
            "#...##.#.",
            "#.....#.#",
            ".#.#####.",
            "..#.#####",
            "...##.##.",
            "....###..",
        ]))

    def test_lit_pixel_count(self):
        for _ in range(2):
            self.enhancer.enhance()

        self.assertEqual(self.enhancer.lit_pixel_count, 35)


if __name__ == '__main__':
    unittest.main()
