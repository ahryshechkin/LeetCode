from unittest import TestCase, main
from tasks.sec_0500.task_0102_binary_tree_level_order_traversal import Solution


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        n1 = TreeNode(15)
        n2 = TreeNode(7)
        n3 = TreeNode(20, n1, n2)
        n4 = TreeNode(9)

        given = TreeNode(3, n4, n3)
        expected = [[3], [9, 20], [15, 7]]
        actual = self.s.levelOrder(given)

        self.assertListEqual(actual, expected)


    def test02(self):
        given = TreeNode(1)
        expected = [[1]]
        actual = self.s.levelOrder(given)

        self.assertListEqual(actual, expected)


    def test03(self):
        given = None
        expected = []
        actual = self.s.levelOrder(given)

        self.assertListEqual(actual, expected)


if __name__ == '__main__':
    main()
