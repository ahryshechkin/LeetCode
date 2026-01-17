from unittest import TestCase, main
from tasks.sec_2000.task_1701_average_waiting_time import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        actual = self.s.averageWaitingTime([[1, 2], [2, 5], [4, 3]])
        self.assertEqual(r, 5.0)

    def test02(self):
        actual = self.s.averageWaitingTime([[5, 2], [5, 4], [10, 3], [20, 1]])
        self.assertEqual(r, 3.25)


if __name__ == '__main__':
    main()
