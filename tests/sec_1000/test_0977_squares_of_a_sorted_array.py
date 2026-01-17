from unittest import TestCase, main
from tasks.sec_1000.task_0977_squares_of_a_sorted_array import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [-4, -1, 0, 3, 10]
        expected = [0, 1, 9, 16, 100]
        actual = self.s.sortedSquares(given)

        self.assertListEqual(actual, expected)


    def test02(self):
        given = [-7, -3, 2, 3, 11]
        expected = [4, 9, 9, 49, 121]
        actual = self.s.sortedSquares(given)

        self.assertListEqual(actual, expected)


if __name__ == '__main__':
    main()
