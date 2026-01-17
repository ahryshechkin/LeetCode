from unittest import TestCase, main
from tasks.sec_1500.task_1295_find_numbers_with_even import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [12, 345, 2, 6, 7896]
        actual = self.s.findNumbers(given)

        self.assertEqual(actual, 2)


    def test02(self):
        given = [555, 901, 482, 1771]
        actual = self.s.findNumbers(given)

        self.assertEqual(actual, 1)


if __name__ == '__main__':
    main()
