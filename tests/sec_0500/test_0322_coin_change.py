from unittest import TestCase, main
from tasks.sec_0500.task_0322_coin_change import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [1, 2, 5]
        amount = 11
        self.assertEqual(self.s.coinChange(given, amount), 3)


    def test02(self):
        given = [3]
        amount = 2
        self.assertEqual(self.s.coinChange(given, amount), -1)


    def test03(self):
        given = [1]
        amount = 0
        self.assertEqual(self.s.coinChange(given, amount), 0)


if __name__ == '__main__':
    main()
