from unittest import TestCase, main
from tasks.sec_0500.task_0001_two_sum import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        actual = self.s.twoSum([2, 7, 11, 15], 9)
        self.assertListEqual(r, [0, 1])


    def test02(self):
        actual = self.s.twoSum([3, 2, 4], 6)
        self.assertListEqual(r, [1, 2])


    def test03(self):
        actual = self.s.twoSum([3, 3], 6)
        self.assertListEqual(r, [0, 1])


if __name__ == '__main__':
    main()
