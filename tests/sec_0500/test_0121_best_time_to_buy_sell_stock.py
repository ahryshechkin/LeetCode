from unittest import TestCase, main
from tasks.sec_0500.task_0121_best_time_to_buy_sell_stock import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(self.s.maxProfit(prices), 5)


    def test02(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(self.s.maxProfit(prices), 0)


if __name__ == '__main__':
    main()
