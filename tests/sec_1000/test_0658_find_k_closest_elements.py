from unittest import TestCase, main
from tasks.sec_1000.task_0658_find_k_closest_elements import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.findClosestElements([1, 2, 3, 4, 5], 4, 3)
        self.assertListEqual(r, [1, 2, 3, 4])

    def test02(self):
        r = self.s.findClosestElements([1, 1, 2, 3, 4, 5], 4, -1)
        self.assertListEqual(r, [1, 1, 2, 3])

    def test03(self):
        r = self.s.findClosestElements([1, 2], 1, 1)
        self.assertListEqual(r, [1])

    def test04(self):
        r = self.s.findClosestElements([1], 1, 1)
        self.assertListEqual(r, [1])

    def test05(self):
        r = self.s.findClosestElements([1, 1, 1, 10, 10, 10], 1, 9)
        self.assertListEqual(r, [10])

    def test06(self):
        r = self.s.findClosestElements([0, 1, 1, 1, 2, 3, 6, 7, 8, 9], 9, 4)
        self.assertListEqual(r, [0, 1, 1, 1, 2, 3, 6, 7, 8])


if __name__ == '__main__':
    main()
