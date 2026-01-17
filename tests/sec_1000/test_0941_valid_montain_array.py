from unittest import TestCase, main
from tasks.sec_1000.task_0941_valid_montain_array import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [2, 1]
        actual = self.s.validMountainArray(given)

        self.assertFalse(actual)


    def test02(self):
        given = [3, 5, 5]
        actual = self.s.validMountainArray(given)

        self.assertFalse(actual)


    def test03(self):
        given = [0, 3, 2, 1]
        actual = self.s.validMountainArray(given)

        self.assertTrue(actual)


    def test04(self):
        given = [2]
        actual = self.s.validMountainArray(given)

        self.assertFalse(actual)


    def test05(self):
        given = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        actual = self.s.validMountainArray(given)

        self.assertFalse(actual)


    def test06(self):
        given = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        actual = self.s.validMountainArray(given)

        self.assertFalse(actual)


if __name__ == '__main__':
    main()
