from unittest import TestCase, main
from tasks.sec_0500.task_0236_lowest_common_ansector_of_binary_tree import Solution


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        n6 = TreeNode(6)
        n7 = TreeNode(7)
        n4 = TreeNode(4)
        n2 = TreeNode(2, n7, n4)
        n5 = TreeNode(5, n6, n2)
        n0 = TreeNode(0)
        n8 = TreeNode(8)
        n1 = TreeNode(1, n0, n8)
        n3 = TreeNode(3, n5, n1)

        actual = self.s.lowestCommonAncestor(n3, n5, n1)
        self.assertEqual(actual.val, n3.val)


    def test02(self):
        n6 = TreeNode(6)
        n7 = TreeNode(7)
        n4 = TreeNode(4)
        n2 = TreeNode(2, n7, n4)
        n5 = TreeNode(5, n6, n2)
        n0 = TreeNode(0)
        n8 = TreeNode(8)
        n1 = TreeNode(1, n0, n8)
        n3 = TreeNode(3, n5, n1)

        actual = self.s.lowestCommonAncestor(n3, n5, n4)
        self.assertEqual(actual.val, n5.val)


if __name__ == '__main__':
    main()
