from unittest import TestCase, main
from tasks.sec_1500.task_1386_cinema_seat_allocation import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.maxNumberOfFamilies(3, [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]])
        self.assertEqual(r, 4)

    def test02(self):
        r = self.s.maxNumberOfFamilies(2, [[2, 1], [1, 8], [2, 6]])
        self.assertEqual(r, 2)

    def test03(self):
        r = self.s.maxNumberOfFamilies(4, [[4, 3], [1, 4], [4, 6], [1, 7]])
        self.assertEqual(r, 4)


if __name__ == '__main__':
    main()
