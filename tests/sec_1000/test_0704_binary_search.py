from unittest import TestCase, main
from tasks.sec_1000.task_0704_binary_search import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [-1, 0, 3, 5, 9, 12]
        actual = self.s.search(given, 9)

        self.assertEqual(actual, 4)


    def test02(self):
        given = [-1, 0, 3, 5, 9, 12]
        actual = self.s.search(given, 2)

        self.assertEqual(actual, -1)


if __name__ == '__main__':
    main()
