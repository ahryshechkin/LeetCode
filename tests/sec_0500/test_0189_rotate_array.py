from unittest import TestCase, main
from tasks.sec_0500.task_0189_rotate_array import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [1, 2, 3, 4, 5, 6, 7]
        expected = [5, 6, 7, 1, 2, 3, 4]

        self.s.rotate(given, 3)
        self.assertListEqual(given, expected)


    def test02(self):
        given = [-1, -100, 3, 99]
        expected = [3, 99, -1, -100]

        self.s.rotate(given, 2)
        self.assertListEqual(given, expected)


if __name__ == '__main__':
    main()
