from unittest import TestCase, main
from tasks.sec_0500.task_0153_find_minimum_in_rotated_sorted_array import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [3, 4, 5, 1, 2]
        expected = 1
        actual = self.s.findMin(given)

        self.assertEqual(actual, expected)


    def test02(self):
        given = [4, 5, 6, 7, 0, 1, 2]
        expected = 0
        actual = self.s.findMin(given)

        self.assertEqual(actual, expected)


    def test03(self):
        given = [11, 13, 15, 17]
        expected = 11
        actual = self.s.findMin(given)

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    main()
