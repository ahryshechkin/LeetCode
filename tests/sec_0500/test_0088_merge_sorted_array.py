from unittest import TestCase, main
from tasks.sec_0500.task_0088_merge_sorted_array import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given1 = [1, 2, 3, 0, 0, 0]
        given2 = [2, 5, 6]
        expected = [1, 2, 2, 3, 5, 6]

        self.s.merge(given1, 3, given2, 3)
        self.assertListEqual(given1, expected)


    def test02(self):
        given1 = [1]
        given2 = []
        expected = [1]

        self.s.merge(given1, 1, given2, 0)
        self.assertListEqual(given1, expected)


    def test03(self):
        given1 = [0]
        given2 = [1]
        expected = [1]

        self.s.merge(given1, 0, given2, 1)
        self.assertListEqual(given1, expected)


if __name__ == '__main__':
    main()
