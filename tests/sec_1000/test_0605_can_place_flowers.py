from unittest import TestCase, main
from tasks.sec_1000.task_0605_can_place_flowers import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        actual = self.s.canPlaceFlowers([1, 0, 0, 0, 1], 1)
        self.assertTrue(actual)


    def test02(self):
        actual = self.s.canPlaceFlowers([1, 0, 0, 0, 1], 2)
        self.assertFalse(actual)


    def test03(self):
        actual = self.s.canPlaceFlowers([1, 0, 0, 0, 0, 0, 1], 2)
        self.assertTrue(actual)


    def test04(self):
        actual = self.s.canPlaceFlowers([1], 0)
        self.assertTrue(actual)


if __name__ == '__main__':
    main()
