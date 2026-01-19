from unittest import TestCase, main
from tasks.sec_0500.task_0198_house_robber import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [1, 2, 3, 1]
        self.assertEqual(self.s.rob(given), 4)


    def test02(self):
        given = [2, 7, 9, 3, 1]
        self.assertEqual(self.s.rob(given), 12)


    def test03(self):
        given = [0]
        self.assertEqual(self.s.rob(given), 0)


if __name__ == '__main__':
    main()
