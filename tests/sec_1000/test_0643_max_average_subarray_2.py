from unittest import TestCase, main
from tasks.sec_1000.task_0643_max_average_subarray_2 import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        actual = self.s.findMaxAverage([1, 12, -5, -6, 50, 3], 4)
        self.assertEqual(actual, 12.75)


    def test02(self):
        actual = self.s.findMaxAverage([5], 1)
        self.assertEqual(actual, 5.00)


    def test03(self):
        actual = self.s.findMaxAverage([-1], 1)
        self.assertEqual(actual, -1.00)


if __name__ == '__main__':
    main()
