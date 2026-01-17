from unittest import TestCase, main
from tasks.sec_0500.task_0001_two_sum import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        expected = [0, 1]
        actual = self.s.twoSum([2, 7, 11, 15], 9)

        self.assertListEqual(actual, expected)


    def test02(self):
        expected = [1, 2]
        actual = self.s.twoSum([3, 2, 4], 6)

        self.assertListEqual(actual, expected)


    def test03(self):
        expected = [0, 1]
        actual = self.s.twoSum([3, 3], 6)

        self.assertListEqual(actual, expected)


if __name__ == '__main__':
    main()
