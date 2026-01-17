from unittest import TestCase, main
from tasks.sec_1500.task_1051_height_checker import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [1, 1, 4, 2, 1, 3]
        actual = self.s.heightChecker(given)

        self.assertEqual(actual, 3)


    def test02(self):
        given = [5, 1, 2, 3, 4]
        actual = self.s.heightChecker(given)

        self.assertEqual(actual, 5)


    def test03(self):
        given = [1, 2, 3, 4, 5]
        actual = self.s.heightChecker(given)

        self.assertEqual(actual, 0)


if __name__ == '__main__':
    main()
