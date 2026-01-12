from unittest import TestCase, main
from tasks.sec_1500.task_1295_find_numbers_with_even import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.findNumbers([12, 345, 2, 6, 7896])
        self.assertEqual(r, 2)

    def test02(self):
        r = self.s.findNumbers([555, 901, 482, 1771])
        self.assertEqual(r, 1)


if __name__ == '__main__':
    main()
