import unittest
from part1 import *


class TestPart1(unittest.TestCase):
    def test1(self):
        node1 = Node.from_list([1, 2])
        node2 = Node.from_list([[3, 4], 5])

        self.assertEqual(add_pairs(node1, node2).as_list(),
                         [[1, 2], [[3, 4], 5]])

    def assert_reduces(self, source: list, target: list):
        node = Node.from_list(source)
        reduce_pair(node)
        self.assertEqual(node.as_list(), target)

    def test2(self):
        self.assert_reduces([[[[[9, 8], 1], 2], 3], 4], [[[[0, 9], 2], 3], 4])

    def test3(self):
        self.assert_reduces([7, [6, [5, [4, [3, 2]]]]], [7, [6, [5, [7, 0]]]])

    def test4(self):
        self.assert_reduces([[6, [5, [4, [3, 2]]]], 1], [[6, [5, [7, 0]]], 3])

    def test5(self):
        self.assert_reduces([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]], [
                            [3, [2, [8, 0]]], [9, [5, [7, 0]]]])

    def test6(self):
        self.assert_reduces([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]], [
                            [3, [2, [8, 0]]], [9, [5, [7, 0]]]])

    def test7(self):
        node1 = Node.from_list([[[[4, 3], 4], 4], [7, [[8, 4], 9]]])
        node2 = Node.from_list([1, 1])

        self.assertEqual(add_pairs(node1, node2).as_list(), [
                         [[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]])

    def assert_reduced_list(self, nodes_list: list, expected: list):
        nodes = [Node.from_list(x) for x in nodes_list]
        self.assertEqual(reduce(add_pairs, nodes).as_list(), expected)

    def test8(self):
        self.assert_reduced_list([[1, 1], [2, 2], [3, 3], [4, 4]], [
            [[[1, 1], [2, 2]], [3, 3]], [4, 4]])

    def test9(self):
        self.assert_reduced_list([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], [
                                 [[[3, 0], [5, 3]], [4, 4]], [5, 5]])

    def test10(self):
        self.assert_reduced_list([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]], [
                                 [[[5, 0], [7, 4]], [5, 5]], [6, 6]])

    def test11(self):
        nodes = [Node.from_list(x) for x in [
            [[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]],
            [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]],
            [[2, [[0, 8], [3, 4]]], [[[6, 7], 1], [7, [1, 6]]]],
            [[[[2, 4], 7], [6, [0, 5]]], [[[6, 8], [2, 8]], [[2, 1], [4, 5]]]],
            [7, [5, [[3, 8], [1, 4]]]],
            [[2, [2, 2]], [8, [8, 1]]],
            [2, 9],
            [1, [[[9, 3], 9], [[9, 0], [0, 7]]]],
            [[[5, [7, 4]], 7], 1],
            [[[[4, 2], 2], 6], [8, 7]]
        ]]

        expected = [
            [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]],
                [[8, [7, 7]], [[7, 9], [5, 0]]]],
            [[[[6, 7], [6, 7]], [[7, 7], [0, 7]]], [
                [[8, 7], [7, 7]], [[8, 8], [8, 0]]]],
            [[[[7, 0], [7, 7]], [[7, 7], [7, 8]]], [
                [[7, 7], [8, 8]], [[7, 7], [8, 7]]]],
            [[[[7, 7], [7, 8]], [[9, 5], [8, 7]]], [
                [[6, 8], [0, 8]], [[9, 9], [9, 0]]]],
            [[[[6, 6], [6, 6]], [[6, 0], [6, 7]]],
                [[[7, 7], [8, 9]], [8, [8, 1]]]],
            [[[[6, 6], [7, 7]], [[0, 7], [7, 7]]], [[[5, 5], [5, 6]], 9]],
            [[[[7, 8], [6, 7]], [[6, 8], [0, 8]]], [
                [[7, 7], [5, 0]], [[5, 5], [5, 6]]]],
            [[[[7, 7], [7, 7]], [[8, 7], [8, 7]]], [[[7, 0], [7, 7]], 9]],
            [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]
        ]

        current = nodes[0]
        for i in range(1, len(nodes)):
            current = add_pairs(current, nodes[i])
            self.assertEqual(current.as_list(),
                             expected[i - 1], "Failed at step %d" % i)


if __name__ == '__main__':
    unittest.main()
