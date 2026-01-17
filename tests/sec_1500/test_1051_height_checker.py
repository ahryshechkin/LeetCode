from unittest import TestCase, main
from tasks.sec_1500.task_1051_height_checker import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        actual = self.s.heightChecker([1, 1, 4, 2, 1, 3])
        self.assertEqual(r, 3)

    def test02(self):
        actual = self.s.heightChecker([5, 1, 2, 3, 4])
        self.assertEqual(r, 5)

    def test03(self):
        actual = self.s.heightChecker([1, 2, 3, 4, 5])
        self.assertEqual(r, 0)


if __name__ == '__main__':
    main()
