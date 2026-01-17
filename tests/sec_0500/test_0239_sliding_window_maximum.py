from unittest import TestCase, main
from tasks.sec_0500.task_0239_sliding_window_maximum import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [1, 3, -1, -3, 5, 3, 6, 7]
        expected = [3, 3, 5, 5, 6, 7]
        actual = self.s.maxSlidingWindow(given, 3)

        self.assertListEqual(actual, expected)


    def test02(self):
        given = [1]
        expected = [1]
        actual = self.s.maxSlidingWindow(given, 1)

        self.assertListEqual(actual, expected)


if __name__ == '__main__':
    main()
