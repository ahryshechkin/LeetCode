from unittest import TestCase, main
from tasks.sec_1000.task_0905_sort_array_by_parity import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [3, 1, 2, 4]
        expected = [2, 4, 3, 1]

        self.s.sortArrayByParity(given)
        self.assertListEqual(given, expected)


    def test02(self):
        given = [0]
        expected = [0]

        self.s.sortArrayByParity(given)
        self.assertListEqual(given, expected)


    def test03(self):
        given = [3, 1]
        expected = [3, 1]

        self.s.sortArrayByParity(given)
        self.assertListEqual(given, expected)


if __name__ == '__main__':
    main()
