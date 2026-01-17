from unittest import TestCase, main
from tasks.sec_0500.task_0003_longest_string_without_repeating_characters import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        actual = self.s.lengthOfLongestSubstring("abcabcbb")
        self.assertEqual(actual, 3)


    def test02(self):
        actual = self.s.lengthOfLongestSubstring("bbbbb")
        self.assertEqual(actual, 1)


    def test03(self):
        actual = self.s.lengthOfLongestSubstring("pwwkew")
        self.assertEqual(actual, 3)


    def test04(self):
        actual = self.s.lengthOfLongestSubstring("au")
        self.assertEqual(actual, 2)


if __name__ == '__main__':
    main()
