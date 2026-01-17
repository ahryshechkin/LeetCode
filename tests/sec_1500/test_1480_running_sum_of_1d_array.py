from unittest import TestCase, main
from tasks.sec_1500.task_1480_running_sum_of_1d_array import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [1, 2, 3, 4]
        expected = [1, 3, 6, 10]
        actual = self.s.runningSum(given)

        self.assertListEqual(actual, expected)


    def test02(self):
        given = [1, 1, 1, 1, 1]
        expected = [1, 2, 3, 4, 5]
        actual = self.s.runningSum(given)

        self.assertListEqual(actual, expected)


    def test03(self):
        given = [3, 1, 2, 10, 1]
        expected = [3, 4, 6, 16, 17]
        actual = self.s.runningSum(given)

        self.assertListEqual(actual, expected)


if __name__ == '__main__':
    main()
