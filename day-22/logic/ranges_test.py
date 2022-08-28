import unittest
from ranges import combine_ranges, DisjointRangesError


class TestCombineRanges(unittest.TestCase):
    # The comments preceding test functions graphically illustrate the
    # relationship between ranges being tested, with both sides being inclusive

    # |-----|
    # |-----|
    def test_when_ranges_identical_returns_range(self):
        self.assertEqual(range(1, 10), combine_ranges(
            range(1, 10), range(1, 10)))

    # |-----|
    #           |-----|
    def test_when_ranges_are_disjoint_with_b_more_positive_throws_exception(self):
        with self.assertRaises(DisjointRangesError):
            combine_ranges(range(1, 10), range(20, 30))

    def test_when_ranges_are_disjoint_with_a_more_positive_throws_exception(self):
        with self.assertRaises(DisjointRangesError):
            combine_ranges(range(20, 30), range(1, 10))

    # |--------|
    #    |--|
    def test_when_a_contains_b_returns_a(self):
        self.assertEqual(range(1, 20), combine_ranges(
            range(1, 20), range(5, 10)))

    def test_when_b_contains_a_returns_a(self):
        self.assertEqual(range(1, 20), combine_ranges(
            range(6, 15), range(1, 20)))

    # |-----|
    #        |-----|
    def test_when_b_follows_a(self):
        self.assertEqual(range(1, 30), combine_ranges(
            range(1, 20), range(20, 30)))

    def test_when_a_follows_b(self):
        self.assertEqual(range(1, 30), combine_ranges(
            range(20, 30), range(1, 20)))

    # |-----|
    #    |-----|
    def test_when_rightside_of_a_overlaps_with_b(self):
        self.assertEqual(range(1, 100), combine_ranges(
            range(1, 50), range(20, 100)))

    def test_when_leftside_of_a_overlaps_with_b(self):
        self.assertEqual(range(1, 100), combine_ranges(
            range(20, 100), range(1, 50)))


if __name__ == '__main__':
    unittest.main()
