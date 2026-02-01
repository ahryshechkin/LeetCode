from unittest import TestCase, main
from tasks.sec_0500.task_0028_find_the_index_in_string import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        haystack = "sadbutsad"
        needle = "sad"
        self.assertEqual(self.s.strStr(haystack, needle), 0)


    def test02(self):
        haystack = "leetcode"
        needle = "leeto"
        self.assertEqual(self.s.strStr(haystack, needle), -1)


if __name__ == '__main__':
    main()
