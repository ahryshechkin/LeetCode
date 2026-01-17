from unittest import TestCase, main
from tasks.sec_0500.task_0056_merge_intervals import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]

        actual = self.s.merge(intervals)

        self.assertEqual(actual, expected)


    def test02(self):
        intervals = [[1, 4], [4, 5]]
        expected = [[1, 5]]

        actual = self.s.merge(intervals)

        self.assertListEqual(actual, expected)


    def test03(self):
        intervals = [[1, 4], [0, 4]]
        expected = [[0, 4]]

        actual = self.s.merge(intervals)

        self.assertListEqual(actual, expected)


if __name__ == '__main__':
    main()
