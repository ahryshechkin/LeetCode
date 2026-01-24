from unittest import TestCase, main
from tasks.sec_0500.task_0048_rotate_image import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]

        self.s.rotate(given)
        self.assertListEqual(given, expected)


    def test02(self):
        given = [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]
        ]
        expected = [
            [15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7, 10, 11]
        ]

        self.s.rotate(given)
        self.assertListEqual(given, expected)


if __name__ == '__main__':
    main()