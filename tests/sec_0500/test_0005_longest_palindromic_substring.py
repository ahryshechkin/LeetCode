from unittest import TestCase, main
from tasks.sec_0500.task_0005_longest_palindromic_substring import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        actual = self.s.longestPalindrome("babad")
        self.assertEqual(r, "bab")


    def test02(self):
        actual = self.s.longestPalindrome("cbbd")
        self.assertEqual(r, "bb")


if __name__ == '__main__':
    main()
