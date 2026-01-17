from unittest import TestCase, main
from tasks.sec_0500.task_0350_intersection_of_two_arrays_2 import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        expected = [2, 2]
        actual = self.s.intersect([1, 2, 2, 1], [2, 2])

        self.assertListEqual(actual, expected)


    def test02(self):
        expected = [4, 9]
        actual = self.s.intersect([4, 9, 5], [9, 4, 9, 8, 4])

        self.assertListEqual(actual, expected)


if __name__ == '__main__':
    main()
