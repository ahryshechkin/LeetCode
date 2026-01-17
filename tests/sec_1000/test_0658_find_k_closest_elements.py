from unittest import TestCase, main
from tasks.sec_1000.task_0658_find_k_closest_elements import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        expected = [1, 2, 3, 4]
        actual = self.s.findClosestElements([1, 2, 3, 4, 5], 4, 3)

        self.assertListEqual(actual, expected)


    def test02(self):
        expected = [1, 1, 2, 3]
        actual = self.s.findClosestElements([1, 1, 2, 3, 4, 5], 4, -1)

        self.assertListEqual(actual, expected)


    def test03(self):
        expected = [1]
        actual = self.s.findClosestElements([1, 2], 1, 1)

        self.assertListEqual(actual, expected)


    def test04(self):
        expected = [1]
        actual = self.s.findClosestElements([1], 1, 1)

        self.assertListEqual(actual, expected)


    def test05(self):
        expected = [10]
        actual = self.s.findClosestElements([1, 1, 1, 10, 10, 10], 1, 9)

        self.assertListEqual(actual, expected)


    def test06(self):
        expected = [0, 1, 1, 1, 2, 3, 6, 7, 8]
        actual = self.s.findClosestElements([0, 1, 1, 1, 2, 3, 6, 7, 8, 9], 9, 4)

        self.assertListEqual(actual, expected)


if __name__ == '__main__':
    main()
