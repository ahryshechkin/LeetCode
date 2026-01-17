from unittest import TestCase, main
from tasks.sec_1000.task_0523_continuous_subarray_sum import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        actual = self.s.checkSubarraySum([23, 2, 4, 6, 7], 6)
        self.assertTrue(actual)


    def test02(self):
        actual = self.s.checkSubarraySum([23, 2, 6, 4, 7], 6)
        self.assertTrue(actual)


    def test03(self):
        actual = self.s.checkSubarraySum([23, 2, 6, 4, 7], 13)
        self.assertFalse(actual)


    def test04(self):
        actual = self.s.checkSubarraySum([23, 2, 4, 6, 6], 7)
        self.assertTrue(actual)


if __name__ == '__main__':
    main()
