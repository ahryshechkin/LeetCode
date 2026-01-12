from unittest import TestCase, main
from tasks.sec_0500.task_0350_intersection_of_two_arrays_2 import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.intersect([1, 2, 2, 1], [2, 2])
        self.assertListEqual(r, [2, 2])

    def test02(self):
        r = self.s.intersect([4, 9, 5], [9, 4, 9, 8, 4])
        self.assertListEqual(r, [4, 9])


if __name__ == '__main__':
    main()
