from unittest import TestCase, main
from tasks.sec_0500.task_0438_find_all_anagrams import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        expected = [0, 6]
        actual = self.s.findAnagrams("cbaebabacd", "abc")

        self.assertListEqual(actual, expected)


    def test02(self):
        expected = [0, 1, 2]
        actual = self.s.findAnagrams("abab", "ab")

        self.assertListEqual(actual, expected)


if __name__ == '__main__':
    main()
