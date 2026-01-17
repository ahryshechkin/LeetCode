from unittest import TestCase, main
from tasks.sec_0500.task_0283_move_zeroes import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [0, 1, 0, 3, 12]
        expected = [1, 3, 12, 0, 0]

        self.s.moveZeroes(given)
        self.assertListEqual(given, expected)


    def test02(self):
        given = [0]
        expected = [0]

        self.s.moveZeroes(given)
        self.assertListEqual(given, expected)


    def test03(self):
        given = [2, 1]
        expected = [2, 1]

        self.s.moveZeroes(given)
        self.assertListEqual(given, expected)


    def test04(self):
        given = [1, 0, 1]
        expected = [1, 1, 0]

        self.s.moveZeroes(given)
        self.assertListEqual(given, expected)


    def test05(self):
        given = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
        expected = [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]

        self.s.moveZeroes(given)
        self.assertListEqual(given, expected)


if __name__ == '__main__':
    main()
