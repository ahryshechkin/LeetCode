from unittest import TestCase, main
from tasks.sec_0500.task_0300_longest_increasing_subsequence import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = [10, 9, 2, 5, 3, 7, 101, 18]
        self.assertEqual(self.s.lengthOfLIS(given), 4)


    def test02(self):
        given = [0, 1, 0, 3, 2, 3]
        self.assertEqual(self.s.lengthOfLIS(given), 4)


    def test03(self):
        given = [7, 7, 7, 7, 7, 7, 7]
        self.assertEqual(self.s.lengthOfLIS(given), 1)


if __name__ == '__main__':
    main()
