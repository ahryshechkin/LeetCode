from unittest import TestCase, main
from tasks.sec_1500.task_1089_duplicate_zeros import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [1, 0, 2, 3, 0, 4, 5, 0]
        expected = [1, 0, 0, 2, 3, 0, 0, 4]

        self.s.duplicateZeros(given)
        self.assertListEqual(given, expected)


    def test02(self):
        given = [1, 2, 3]
        expected = [1, 2, 3]

        self.s.duplicateZeros(given)
        self.assertListEqual(given, expected)


if __name__ == '__main__':
    main()
