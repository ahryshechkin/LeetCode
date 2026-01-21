from unittest import TestCase, main
from tasks.sec_0500.task_0004_median_of_two_sorted_arrays import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        actual = self.s.findMedianSortedArrays([1, 3], [2])
        self.assertEqual(actual, 2)


    def test02(self):
        actual = self.s.findMedianSortedArrays([1, 2], [3, 4])
        self.assertEqual(actual, 2.5)


if __name__ == '__main__':
    main()
