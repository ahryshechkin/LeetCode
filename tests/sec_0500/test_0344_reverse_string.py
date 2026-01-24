from unittest import TestCase, main
from tasks.sec_0500.task_0344_reverse_string import Solution


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        given = ["h", "e", "l", "l", "o"]
        expected = ["o", "l", "l", "e", "h"]

        self.s.reverseString(given)
        self.assertListEqual(given, expected)


    def test02(self):
        given = ["H", "a", "n", "n", "a", "h"]
        expected = ["h", "a", "n", "n", "a", "H"]

        self.s.reverseString(given)
        self.assertListEqual(given, expected)


if __name__ == '__main__':
    main()
