from unittest import TestCase, main
from tasks.sec_0500.task_0414_third_maximum_number import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [3, 2, 1]
        self.assertEqual(self.s.thirdMax(given), 1)


    def test02(self):
        given = [1, 2]
        self.assertEqual(self.s.thirdMax(given), 2)


    def test03(self):
        given = [2, 2, 3, 1]
        self.assertEqual(self.s.thirdMax(given), 1)


if __name__ == '__main__':
    main()
