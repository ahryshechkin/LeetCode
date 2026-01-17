from unittest import TestCase, main
from tasks.sec_0500.task_0448_find_disappeared_numbers import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [4, 3, 2, 7, 8, 2, 3, 1]
        expected = [5, 6]
        actual = self.s.findDisappearedNumbers(given)

        self.assertListEqual(actual, expected)


    def test02(self):
        given = [1, 1]
        expected = [2]
        actual = self.s.findDisappearedNumbers(given)

        self.assertListEqual(actual, expected)


if __name__ == '__main__':
    main()
