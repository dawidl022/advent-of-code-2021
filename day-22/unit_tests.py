import unittest
from part1 import Area3D


class TestArea3D(unittest.TestCase):
    def setUp(self):
        unittest.util._MAX_LENGTH = 2000
        self.area_3d = Area3D()

    def test_area_initially_zero(self):
        self.assertEqual(0, self.area_3d.area)

    def test_area_after_adding_range(self):
        self.area_3d.add_range(range(10, 13), range(10, 13), range(10, 13))
        self.assertEqual(27, self.area_3d.area)

    def test_area_after_adding_two_ranges(self):
        self.area_3d.add_range(range(10, 13), range(10, 13), range(10, 13))
        self.area_3d.add_range(range(11, 14), range(11, 14), range(11, 14))
        self.assertEqual(27 + 19, self.area_3d.area)

    def test_add_range_when_overlapping_on_all_3_axis(self):
        self.area_3d.add_range(range(10, 13), range(10, 13), range(10, 13))
        self.area_3d.add_range(range(11, 14), range(11, 14), range(11, 14))
        self.assertEqual(
            {(range(10, 14), range(10, 14), range(10, 14))},
            set(self.area_3d.on)
        )

    def test_add_range_when_overlapping_on_2_axis(self):
        pass

    def test_add_range_when_disjoint(self):
        pass


if __name__ == '__main__':
    unittest.main()
