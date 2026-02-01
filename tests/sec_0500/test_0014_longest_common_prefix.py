from unittest import TestCase, main
from tasks.sec_0500.task_0014_longest_common_prefix import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = ["flower", "flow", "flight"]
        expected = "fl"
        actual = self.s.longestCommonPrefix(given)

        self.assertEqual(actual, expected)


    def test02(self):
        given = ["dog", "racecar", "car"]
        expected = ""
        actual = self.s.longestCommonPrefix(given)

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    main()
